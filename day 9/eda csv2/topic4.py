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
# TOPIC 4 — CORRELATION ANALYSIS
# ----------------------------------------------------------

# Correlation matrix (numerical columns only)
corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

# HEATMAP — visualize correlations
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
