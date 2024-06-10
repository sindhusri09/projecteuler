def find_pythagorean_triplet(target_sum):
    for a in range(1, target_sum):
        for b in range(a + 1, target_sum):
            c = target_sum - a - b
            if c > 0:
                if a**2 + b**2 == c**2:
                    return a, b, c

target_sum = 1000
a, b, c = find_pythagorean_triplet(target_sum)
product_abc = a * b * c
print("Pythagorean triplet:", a, b, c)
print("Product abc:", product_abc)
