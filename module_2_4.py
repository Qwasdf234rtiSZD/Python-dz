numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
n = 0

primes = []
not_primes = []
i = 0            # Счётчик

for i in range(len( numbers )):
    is_prime = True
    n = numbers[i]

    if n < 2:
        print(n, '- не простое и не сложное число')
        continue

    else:
        f = n ** (1 / 2)  # Квадратный корень из n
        for a in range( 2, int(f + 1) ):
            if n % a == 0:
                is_prime = False
                break
    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True  # признак простого числа
print('Primes ', primes)
print('Not Primes ', not_primes)