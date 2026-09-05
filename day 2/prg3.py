x = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    x.append(num)

print("\nEntered List:", x)
print("Minimum value:", min(x))
print("Maximum value:", max(x))
print("Sum:", sum(x))
print("Average:", sum(x) / len(x))
print("Total Length:", len(x))
print("Sorted List:", sorted(x))