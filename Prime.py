def largest_prime_factor(n):
    i = 2
    largest_factor = 1
    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        largest_factor = n
    return largest_factor
number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is", result)
