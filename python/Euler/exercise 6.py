from_number = 2
to_number = 20

number = []
def prime_numbers(x):
    solution = []
    for i in range(2,x):
        if (x % i == 0 and x != i):
            solution.insert(prime_numbers(i))
        elif x % i == 0:
            return x
    return solution

test = prime_numbers(10)