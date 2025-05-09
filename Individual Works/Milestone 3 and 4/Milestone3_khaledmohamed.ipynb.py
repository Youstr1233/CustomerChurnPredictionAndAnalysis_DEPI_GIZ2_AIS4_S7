import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Step 2: Basic data info
def basic_info(data):
    print("\nBasic Information:")
    print(data.info())
    print("\nStatistical Summary:")
    print(data.describe())

# Step 3: Check for missing values
def check_missing(data, columns):
    missing = data[columns].isnull().sum()
    print("\nMissing Values:")
    print(missing)

# Step 4: Handle missing values
def handle_missing(data):
    data['age'].fillna(data['age'].median(), inplace=True)
    data['gender'].fillna(data['gender'].mode()[0], inplace=True)
    data['telecom_partner'].fillna('Unknown', inplace=True)
    data['age_decay_range'].fillna(data['age_decay_range'].median(), inplace=True)
    data['age_interval'].fillna(data['age_interval'].median(), inplace=True)
    print("\nMissing values handled.")

# Step 5: Check for negative values
def check_negative(data, columns):
    negative_counts = {col: (data[col] < 0).sum() for col in columns}
    print("\nNegative Values:")
    print(negative_counts)

# Step 6: Handle negative values
def handle_negative(data):
    data['age'] = data['age'].abs()
    data['age_decay_range'] = data['age_decay_range'].abs()
    data['age_interval'] = data['age_interval'].abs()
    print("\nNegative values handled.")

# Step 7: Visualization
def visualize_data(data):
    plt.figure(figsize=(15, 10))
    sns.histplot(data['age'], kde=True)
    plt.title('Distribution of Age')
    plt.show()

    plt.figure(figsize=(12, 5))
    sns.countplot(data=data, x='gender')
    plt.title('Gender Distribution')
    plt.show()

    plt.figure(figsize=(12, 5))
    sns.countplot(data=data, x='telecom_partner')
    plt.title('Telecom Partner Distribution')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.heatmap(data[['age', 'age_decay_range', 'age_interval']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix Heatmap')
    plt.show()

# Main function
def main():
    file_path = input("Enter the file path: ")
    data = load_data(file_path)
    if data is not None:
        basic_info(data)
        check_missing(data, ['telecom_partner', 'gender', 'age', 'age_decay_range', 'age_interval'])
        handle_missing(data)
        check_negative(data, ['age', 'age_decay_range', 'age_interval'])
        handle_negative(data)
        visualize_data(data)

if __name__ == "__main__":
    main()
