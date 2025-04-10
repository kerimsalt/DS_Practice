import seaborn as sns
import numpy as np
df = sns.load_dataset('titanic')
# print(df.head())
# print(df.iloc[0, :5])  # Display the first 5 rows and first 5 columns


def average_age_of_survivors():
    survivors = df[df['survived'] == 1]
    # Calculate the average age of survivors
    print(type(survivors))
    print(len(survivors))
    average_age = survivors['age'].mean()
    print(f"Average age of survivors: {average_age:.2f}")


def survival_rate():
    total = len(df)
    n_survivors = len(df[df["survived"] == 1])
    print(n_survivors/total * 100)


average_age_of_survivors()
sr()