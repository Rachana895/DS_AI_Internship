# for numerical num , we analyze mean,median,skewness,and range.
# for categorical cat , we analyze frequency counts.
# univarate analysis sub topics:
# distribution
# central tendency
# spread
# frequency

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve plot appearance
sns.set(style="whitegrid")

# ---------------------------------------------------------- 
# STEP 2 — Load / Create Dataset
# (In real projects: df = pd.read_csv("dataset.csv"))
# ----------------------------------------------------------
data = {
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Gender": ["M","F","M","M","F","F","M","M","F","F","M","F"]
}

df = pd.DataFrame(data)

# ----------------------------------------------------------
# TOPIC 2 — UNIVARIATE ANALYSIS
# Analyze ONE variable at a time
# ----------------------------------------------------------

# HISTOGRAM — Distribution of Age
plt.figure()
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.show()

# HISTOGRAM — Distribution of Salary
plt.figure()
sns.histplot(df["Salary"], kde=True)
plt.title("Salary Distribution")
plt.show()

# BOXPLOT — Detect spread & outliers in Salary
plt.figure()
sns.boxplot(x=df["Salary"])
plt.title("Salary Boxplot")
plt.show()

# CATEGORICAL ANALYSIS — Frequency counts
print("\nDepartment counts:")
print(df["Department"].value_counts())

print("\nGender counts:")
print(df["Gender"].value_counts())

# Bar plot for categorical variable
plt.figure()
sns.countplot(x="Department", data=df)
plt.title("Department Distribution")
plt.show()

