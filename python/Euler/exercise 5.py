#
#   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

def smallestMultiple(number):
    result = 1
    for i in range(1, number + 1):
        if result % i != 0:
            for j in range(1, i + 1):
                if (result * j) % i == 0:
                    result *= j
                    break
    return result

print(smallestMultiple(20))