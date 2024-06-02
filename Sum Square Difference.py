def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))
def square_of_sum(n):
    return sum(range(1, n+1)) ** 2
n = 100
sum_squares = sum_of_squares(n)
square_sum = square_of_sum(n)
difference = square_sum - sum_squares
print("Difference:",difference)
