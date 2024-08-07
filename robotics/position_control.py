import json, time, os
import numpy as np
import pandas as pd
from robot.robot import Robot

CONVERSION_FACTOR = 4096 / 360

def load_robot_settings():
    """
    Load the config file for the Robot arm instances.

    Inputs:
        None

    Returns:
        arm_config (dict): A dictionary continaing the arm configuration parameters.
    """
    with open('config.json') as f:
        config = json.load(f)
    arm_config = config['arm']
    return arm_config

def initialize_robot(arm_config):
    """
    Creates and initializes a robot instance using the provided arm configuration.

    Arm configuration should include:
        - 'device_name': Name of the port connected to the robot arm.
        - 'baudrate': Bits per second.
        - 'servo_ids': List of servo IDs for the arm.
        - 'velocity_limit': Maximum velocity limit of each servo of the arm.
        - 'max_position_limit': Maximum position limit of each servo of the arm.
        - 'min_position_limit': Minimum position limit of each servo of the arm.

    Inputs:
        arm_config (dict): A dictionary containing the arm configuration parameters.

    Returns:
        arm (object): A conigured (arm) Robot instance.
    """
    arm = Robot(
                arm_config['device_name'],
                arm_config['baudrate'], 
                arm_config['servo_ids'],
                arm_config['velocity_limit'],
                arm_config['max_position_limit'],
                arm_config['min_position_limit']
                )
    return arm

def change_servo_angle(arm, servo_id, delta):
    """
    Adjusts the angle of a specified servo motor by a given delta and prints 
    the updated angles of all servos in the robotic arm instance.

    Inputs:
        arm (object): The robotic arm instance
        servo_id (int): The id of the servo whose angle is to be changed.
        delta (float): The +/- rotation to be applied to the servo motor.

    Returns:
        None
    """
    pos = arm.read_position()
    pos = [int(p) for p in pos]
    servo_id_index = arm.servo_ids.index(servo_id)
    pos[servo_id_index] += delta
    arm.set_and_wait_goal_pos(pos, servo_id=servo_id)
    # Print the current position of the servo after the move
    time.sleep(0.25)
    cur_pos = arm.read_position()
    positions_in_degrees = np.round(np.array(cur_pos) / CONVERSION_FACTOR, 2)
    df = pd.DataFrame({
        'ID': arm.servo_ids,
        'Degrees': positions_in_degrees
    })
    print('\n', df.to_string(index=False), '\n')

def record_action(arm, action, pose_type):
    """
    Updates an existing action or creates a new one if it doesn't exist, 
    and records one of the four pose types for that action.

    An action consists of four pose types:
        - 'hover': Arm placement before attempting to grasp an object.
        - 'pre-grasp': Arm moves into a grasping position.
        - 'grasp': Arm grasps the object.
        - 'post-grasp': Arm lifts the object.
    
    Inputs:
        arm (object): The robotic arm instance.
        action (str): The name of the action to be updated or created.
        pose_type (str): The type of pose to be recorded (one of 'hover', 'pre-grasp', 'grasp', 'post_grasp').

    Returns:
        bool: True for a successful action record, otherwise False
    """
    valid_pose_types = ['hover', 'pre-grasp', 'grasp', 'post-grasp']

    if pose_type not in valid_pose_types:
        print(f"pose_type must be one of {valid_pose_types}")
        return False

    # Create an actions.json file if it does not already exist
    if not os.path.exists('actions.json'):
        with open('actions.json', 'w') as f:
            json.dump({}, f)

    # Load existing actions from the file
    with open('actions.json') as f:
        actions = json.load(f)

    # Read the current position of the arm
    positions = arm.read_position()
    positions = [int(p) for p in positions]

    # Update the action with the specified pose type
    if action not in actions:
        actions[action] = {}

    actions[action][pose_type] = positions

    # Write the updated actions back to the file
    with open('actions.json', 'w') as f:
        json.dump(actions, f, indent=4)

    return True


def initiate_action(arm, action):
    """
    Initiate an action (if present) within the action.json file.

    Inputs:
        arm (object): The robotic arm instance.
        action (str): The name of the action to be executed.
    
    Returns:
        None
    """
    valid_pose_types = ['hover', 'pre-grasp', 'grasp', 'post-grasp']

    # Load existing actions from the file
    with open('actions.json') as f:
        actions = json.load(f)

    if action not in actions:
        print(f"Error: {action} is not a valid action.")
        return

    # Initiate each pose within the provided action
    # Sleep for 0.25 seconds after each pose.
    for pose in valid_pose_types:

        if pose in actions[action]:
            arm.set_and_wait_goal(actions[action][pose])
            time.sleep(0.25)
        else:
            print(f"Error: {pose} is not found, {action} is incomplete.")
            return
    
    print(f"{action} completed successfully.")

def main():
    arm_config = load_robot_settings()
    arm = initialize_robot(arm_config)
    
    # Go to home position
    arm.set_and_wait_goal_pos(arm_config['home_pos'])

    # Position control loop
    print('\n\nWelcome to position control mode!')
    print('Enter "p" to position each motor 1 at a time.')
    print('Enter servo ID and delta angle (in degrees) to move the servo.')
    print('Delta angle can be positive or negative, and the servo angle will change by that amount.')
    print('The current position of the servo will be printed after each move.')
    print('Enter "q" at any time to quit.')
    print('Enter "i" to use a saved action')
    print('Enter "a" at any time to record an action\n\n')

    while True:
        try:
            user_input = input('Enter task: ').lower()
            
            if user_input == 'q':
                break
            elif user_input == 'i':
                action = input('Enter action name')
                initiate_action(arm, action)
            elif user_input == 'p':
                servo_id = int(input("Enter Servo id: "))
                if servo_id not in arm_config['servo_ids']:
                    print(f'Invalid servo ID. Please enter one of {arm_config["servo_ids"]}\n')
                    continue
                delta = float(input('Enter delta angle: '))
                delta = int(delta * CONVERSION_FACTOR)

                change_servo_angle(arm, servo_id, delta)
            # Optionally record an action
            elif user_input.lower() == 'a':
                action_name = input('Enter action name: ')
                pose_type = input('Enter pose type (hover, pre-grasp, grasp, post-grasp): ')
                success = record_action(arm, action_name, pose_type)
                if success:
                   print('Action recording successful')
                else:
                   print('Action recording failed')
        except KeyboardInterrupt:
            break

    # Go to rest position and disable torque
    arm.set_and_wait_goal_pos(arm_config['rest_pos'])
    arm._disable_torque()

if __name__ == '__main__':
    main()