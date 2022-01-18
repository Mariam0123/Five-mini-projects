from random import randint


def roll_dice(sides: int):
    """The function rolls a die and returns the result as an `int`. The input is sides of type `int` representing the number of sides on the die."""
    return randint(1, sides)


if __name__ == "__main__":
    sides_in = int(input("Please enter the number of sides on the die:\t"))
    ans = ""
    while ans != "n".casefold():
        print("..........Rolling die..........")
        print(f"The result is {roll_dice(sides_in)}")
        ans = input("Would you like to roll again? Enter Y for yes and N for no.")
        if ans == "N".casefold():
            print("Thanks for using the program.")
            exit()
