'''
The problem:
"You are given two positive integers a and b (a < b <= 20000). 
Complete the function which returns a list of all those numbers in the interval [a, b) whose digits are made up of prime 
numbers (2, 3, 5, 7) but which are not primes themselves."
From :https://www.codewars.com/kata/5a9a70cf5084d74ff90000f7
'''
def prime_digit_not_prime(a, b):
  result = []
  for num in range(a, b):
    if all(int(digit) in [2, 3, 5, 7] for digit in str(num)) and not all(num % i != 0 for i in range(2, num)):
      result.append(num)
  return result

def main(a, b):
    result = prime_digit_not_prime(a, b)
    for i in range(len(result)):
        print(result[i])

if __name__ == "__main__":
    main(10, 250)


    '''
    the above solution (function prime_digit_not_prime) is made og chatGPT but i think it is not working.... Where is the bug????
    Found it!!!!
    '''
