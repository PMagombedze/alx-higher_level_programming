#!/usr/bin/python3
def fizzbuzz():
    """fizz buzz fizzbuzz"""
    for n in range(1, 101):
        if n % 3 == 0:
            if n % 5 == 0:
                print("FizzBuzz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(f"{n}", end=" ")
