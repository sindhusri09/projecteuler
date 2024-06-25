def sum_of_primes_below(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False  

    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, n, start):
                sieve[multiple] = False

    return sum(index for index, is_prime in enumerate(sieve) if is_prime)

limit = 2000000
result = sum_of_primes_below(limit)
print(result)
