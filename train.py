import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'firsthundered.csv'  # Adjust as per your directory structure
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found at: {file_path}")
    raise

# Example: Display first few rows of the dataset
print(df.head())

# Example: Create a histogram of 'Age'
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
