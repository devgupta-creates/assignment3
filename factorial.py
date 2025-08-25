result = 0
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n= int(input("Enter a number to calculate its factorial: "))
print(f'factorial is {factorial(n)}')
