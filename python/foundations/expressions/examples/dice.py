import random

NUM_SIDES = 6   # constant

def roll_dice():
    """
    Simulate rolling two dice.
    """
    die_1 = random.randint(0, NUM_SIDES)
    die_2 = random.randint(0, NUM_SIDES)

    sum = die_1 + die_2
    return sum

def main():
    roll_dice()

if __name__ == '__main__':
    main()
