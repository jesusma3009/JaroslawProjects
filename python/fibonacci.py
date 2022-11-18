li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def fibo(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibo(n - 1) + fibo(n - 2)

# Generate fibbonaci list
newli = []
for x in li:
  newli.append(fibo(x))
print("Fibbonacci list")
print(newli)

# Generate prime number list
primeli = []
for x in range(2,newli[-1]):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
            else:
                primeli.append(x)
                break
print("Prime number list")
print(primeli)

# List of prime numbers filter with fibonnaci
def filter_primelist(number):
  return number in primeli
filter_list = list(filter(filter_primelist, newli))

print("Filter list")
print(filter_list)
