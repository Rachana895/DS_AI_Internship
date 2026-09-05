import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
             "K", "L", "M", "A", "B"],
    "Marks": [85, 90, None, 75, 88, 92, None, 70, 85, 95,
              80, None, 78, 85, 90],
    "Attendance": [90, 95, 80, None, 88, 92, 85, 75, 90, 98,
                   None, 82, 79, 90, 95]
}

df = pd.DataFrame(data)

print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())