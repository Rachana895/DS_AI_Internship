import pandas as pd

data = pd.read_csv("task2.csv")

print("Original Shape:", data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nTotal Missing Values:", data.isnull().sum().sum())

print("\nDuplicate Records:")
print(data[data.duplicated()])

print("\nNumber of Duplicates:", data.duplicated().sum())

data = data.drop_duplicates()

data["Math"] = data["Math"].fillna(int(data["Math"].mean()))
data["English"] = data["English"].fillna(int(data["English"].mean()))
data["Science"] = data["Science"].fillna(int(data["Science"].mean()))

print("\nCleaned Dataset:")
print(data)

print("\nCleaned Shape:", data.shape)