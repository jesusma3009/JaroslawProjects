#
#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#   What is the 10 001st prime number?
#

#   I'm going to calculate the 10001 first prime numbers and then return the last one.

def primeNumbers(number):
    result = []
    i = 2
    while len(result) < number:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
        i+=1
    return result

print(primeNumbers(10001)[-1])