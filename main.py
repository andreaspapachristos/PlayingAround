# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from math import sqrt




def PerfectNumbers(number):
    sum = 0
    for i in range(2, math.ceil(sqrt(number))):

        if int(number) % i == 0:
            sum += i+(number/i)

    if (sum +1 == number):
        print(number)
    else:
        print("not a perfect number")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(497):
        PerfectNumbers(i)


