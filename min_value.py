#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Dec.15, 2022
# This program generates 10 random numbers and
# prints the lowest out of the list of 10 random numbers

import random
import constants


def min_value(numbers):
    # Set the initial minimum value to the first number in the list
    min_val = numbers[0]

    # Loop through the rest of the numbers in the list
    for num in numbers:
        # If the current number is less than the minimum value, update the minimum value
        if num < min_val:
            min_val = num

    # Return the minimum value
    return min_val


def main():
    random_num_list = []
    # Generate 10 random numbers between 0 and 100
    for counter in range(constants.MAX):

        # generates a number between 0 and 100
        random_num = random.randint(constants.MIN_RAND, constants.MAX_RAND)

        # Adds number to the list
        random_num_list.append(random_num)

        # print that it added the number to the index
        print(f"Added {random_num} to list at index {counter}")

    # call min_value(random_num_list)
    min_val = min_value(random_num_list)

    # print what the lowest value is
    print(f"The lowest number is {min_val}")


if __name__ == "__main__":
    main()
