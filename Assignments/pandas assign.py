import pandas as pd

marks = pd.Series([85, 90, 78, 88],
                  index=["Math", "Python", "DBMS", "Java"])

print(marks)

# Access using positions
print("First marks:", marks.iloc[0])

# Access using label
print("Python marks:", marks["Python"])