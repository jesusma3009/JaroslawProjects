#
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#   Find the sum of all the primes below two million.
#
import math
def primeNumberList(n):
    list = [True for i in range(n+2)]
    for i in range(2, int(math.sqrt(n))):
        if list[i] == True:
            for j in range(i+i, n,i):
                list[j] = False
    result = 0
    for i in range(2,n):
        if(list[i]):
            result += i
    return result


print(primeNumberList(2000000))
