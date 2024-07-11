numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i > 1:
        is_prime = True
        if i > 3:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    is_prime = False
                    break
        if is_prime == True:
            primes.append(i)
        else:
            not_primes.append(i)
        
print(f'Простые числа "primes": {primes}')
print(f'не простые числа "not_primes": {not_primes}')