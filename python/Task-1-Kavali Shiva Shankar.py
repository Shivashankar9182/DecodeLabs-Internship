import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file = 'Dataset for Data Analytics.xlsx'
df = pd.read_excel(file)

# View dataset
print(df.head())
print(df.info())

# Missing values
print(df.isnull().sum())

# Statistics
print(df.describe())

# Correlation
corr = df.corr(numeric_only=True)
print(corr)

# Heatmap
sns.heatmap(corr, annot=True)
plt.show()

# Histogram
plt.hist(df.select_dtypes(include='number').iloc[:,0])
plt.show()

# Boxplot
sns.boxplot(x=df.select_dtypes(include='number').iloc[:,0])
plt.show()