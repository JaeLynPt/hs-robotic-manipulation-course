import math

def main():
    """
    Prompt the user to input the coordinates of two points (x1, y1) and (x2, y2).
    Then, compute the distance using the formula:

        √((x2 - x1)^2 + (y2 - y1)^2)

    Example:
    --------
    Enter x_1: 1
    Enter x_2: 4
    Enter y_1: 2
    Enter y_2: 6
    The distance between the points (1, 2) and (4, 6) is 5.0
    """
    first_point = int(input("Enter the first x coordinate ... : "))
    snd_point = int(input("Enter the first y coordinate .... : "))
    thd_point = int(input("Enter the second x coordinate ... : "))
    frth_point = int(input("Enter the second y coordinate ... : "))

    print(f"The distance between the points ({first_point},{snd_point}) and ({thd_point},{frth_point}) is {math.sqrt((thd_point - first_point)**2 + (frth_point- snd_point)**2)}")
          
main()