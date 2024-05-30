a, b = 1, 2
even_sum = 0
while a <= 4000000:
    if a % 2 == 0:
        even_sum += a
    a, b = b, a + b
print("The sum of the even-valued terms in the Fibonacci sequence not exceeding four million is:", even_sum)
