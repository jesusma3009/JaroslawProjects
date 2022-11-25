#   Find the difference between the sum of the squares of
#   the first one hundred natural numbers and the square of the sum.
n=101
f1 = (n*(n-1)/2)*(n*(n-1)/2)

def f2(a):
    solution = 0
    for i in range(1,a):
        solution += i*i
    return solution

print(f1)
print(f2(n))
print(f1 - f2(n))