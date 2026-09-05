def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


# Main Program
num = int(input("Enter a number: "))
table(num)