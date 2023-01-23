"""
Πρόκειται για μια συνάρτηση που υπολογίζει τους "τέλειους" αριθμούς. Έναυσμα για αυτό ήταν η πρώτη μου επαφή με το
chatGPT στο οποίο "ζήτησα" να μου γραψει την συναρτηση και νομίζω ότι δεν ήταν η βέλτιση λύση
"""
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
    for i in range(49):
        PerfectNumbers(i)


