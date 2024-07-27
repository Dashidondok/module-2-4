numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in numbers:
    if i == 1:
        continue
    is_prime = False
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            break
        else:
            is_prime = False
    if is_prime == False:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)