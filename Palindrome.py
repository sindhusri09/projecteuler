def is_palindrome(num):
    return str(num) == str(num)[::-1]
def largest_palindromic_product():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome
print(largest_palindromic_product())
