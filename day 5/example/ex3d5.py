import math

num = int(input("Enter a number: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
angle = float(input("Enter angle in degrees: "))
radius = float(input("Enter radius: "))
decimal = float(input("Enter a decimal number: "))

print("\n--- Math Module Operations ---")

print("Square root =", math.sqrt(num))
print("Power =", math.pow(num, 2))
print("Factorial =", math.factorial(num))

print("GCD =", math.gcd(a, b))
print("LCM =", math.lcm(a, b))

print("Absolute value =", math.fabs(-num))

print("Ceiling =", math.ceil(decimal))
print("Floor =", math.floor(decimal))

print("Logarithm =", math.log(num))

radian = math.radians(angle)
print("Sin =", math.sin(radian))
print("Cos =", math.cos(radian))
print("Tan =", math.tan(radian))

print("Area of circle =", math.pi * radius * radius)
print("Circumference =", 2 * math.pi * radius)