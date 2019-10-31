#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program does FOR looping


def main():
    answer = 0
    counter = 1


number = int(input("What is your number: "))

for counter in range(number + 1):
    answer = counter * counter
    print(str(counter) + "² = " + str(answer))


if __name__ == "__main__":
    main()
