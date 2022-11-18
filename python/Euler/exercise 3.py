
#  The prime factors of 13195 are 5, 7, 13 and 29.
#
#  What is the largest prime factor of the number 600851475143 ?

number = 600851475143
primeFactor = []

for i in range(2, number):
    while number % i == 0 and number > 1:
        primeFactor.append(i)
        number /= i
        if (number == 1):
            print(primeFactor)
            exit()
