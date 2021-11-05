#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This program uses a list


def calculator(numbers):
    total = 0
    for counter in range(0, len(numbers)):
        total = total + numbers[counter]
    return total


def main():
    # this function uses a list

    numbers = []
    number = None

    # input
    print("Please enter 1 number at a time. Enter 'Stop' to end.\n")

    while True:
        integer = input("Enter number to add: ")
        if integer == "Stop":
            break
        else:
            try:
                number = float(integer)
                numbers.append(number)
            except Exception:
                print("Invalid input")
    summ = calculator(numbers)
    print("\nThe sum is {0}".format(summ))
    print("\nDone.")


if __name__ == "__main__":
    main()
