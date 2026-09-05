def total_marks(m1, m2, m3, m4, m5):
    return m1 + m2 + m3 + m4 + m5

name = input("Enter Student Name: ")

m1 = int(input("Enter Subject 1 Marks: "))
m2 = int(input("Enter Subject 2 Marks: "))
m3 = int(input("Enter Subject 3 Marks: "))
m4 = int(input("Enter Subject 4 Marks: "))
m5 = int(input("Enter Subject 5 Marks: "))

total = total_marks(m1, m2, m3, m4, m5)

print(name)
print("Total Marks:", total)