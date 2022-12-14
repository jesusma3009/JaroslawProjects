#   Project Euler exercise 4
#
#   A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#   Find the largest palindrome made from the product of two 3-digit numbers.
#
solution=0
for i in range(999,100, -1):
    for j in range(i,100, -1):
        if str(i*j) == str(i*j)[::-1]:
            if (solution <= i * j):
                solution = i * j
print(solution)

