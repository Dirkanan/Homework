numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    dividers = set()
    for j in numbers:
        if i % j == 0:
            dividers.add(j)
    if len(dividers) == 2:
        primes.append(i)
    elif len(dividers) > 1:
        not_primes.append(i)
print(primes)
print(not_primes)
