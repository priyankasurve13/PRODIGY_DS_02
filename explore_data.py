import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Step 1: Load dataset
file_path = 'firsthundered.csv'
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"File not found at: {file_path}")
    raise

# Print first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Step 2: Handle missing values
print("\nStep 2: Handling Missing Values")
print("Number of missing values:")
print(df.isnull().sum())

# Fill missing values in 'Age' with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing values in 'Embarked' with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Step 3: Visualize data distribution
print("\nStep 3: Visualizing Data Distribution")

# Histogram of 'Age'
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
print("Plot generated: Age distribution")

# Bar plot of 'Sex'
plt.figure(figsize=(8, 5))
sns.countplot(x='Sex', data=df)
plt.title('Distribution of Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()
print("Plot generated: Sex distribution")

# Step 4: Perform statistical analysis
print("\nStep 4: Performing Statistical Analysis")

# T-test example: Compare 'Fare' between different 'Pclass'
print("\nT-test between Fare and Pclass:")
group1 = df[df['Pclass'] == 1]['Fare']
group2 = df[df['Pclass'] == 2]['Fare']
t_stat, p_value = ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}, p-value: {p_value}")

# Step 5: Documentation and final summary
print("\nStep 5: Documentation and Final Summary")
print("Summary Statistics:")
print(df.describe())

# Documenting the actions taken
print("""
Steps Taken:
1. Loaded dataset 'firsthundered.csv'.
2. Handled missing values in 'Age' and 'Embarked'.
3. Visualized distributions of 'Age' and 'Sex'.
4. Conducted statistical analysis with t-tests.
5. Documented summary statistics.
""")

# Display final dataset information
print("\nFinal Dataset Information:")
print(df.info())
