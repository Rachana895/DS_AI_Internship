# Function to find factorial
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Main Program
num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial of", num, "is", result)
