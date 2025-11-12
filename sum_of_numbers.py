#!/usr/bin/env python3
# Created by: Patrick
# Created on: 11/11/2025
# This program calculates the sum of all whole numbers from 0 to a user-input positive number.


def main():
    # ask user to enter a positive number
    user_number = input("Enter a positive number: ")
    sum = 0

    # calculate the number given by the user and gives the output
    try:
        user_number = int(user_number)
        if user_number < 0:
            print("Please enter a positive integer")
        else:
            counter = 0
            while counter <= user_number:
                sum += counter
                counter += 1
            print("Sum =", sum)
    except ValueError:
        print("Please enter a valid value")


if __name__ == "__main__":
    main()
