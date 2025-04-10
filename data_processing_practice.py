import seaborn as sns
df = sns.load_dataset('titanic')
# print(df.head())
# print(df.iloc[0, :5])  # Display the first 5 rows and first 5 columns
# Assume that the df is global and already loaded


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
    rate = round(n_survivors/total * 100)
    print(f"Survival rate: {rate}%")


def gender_distribution_of_survivors():
    survivors = df[df['survived'] == 1]
    n_males = len(survivors[survivors['sex'] == 'male'])
    n_females = len(survivors[survivors['sex'] == 'female'])
    male_rate = round(n_males / len(survivors) * 100, 2)
    female_rate = round(n_females / len(survivors) * 100, 2)
    print(f"{male_rate}% of the survivors were male")
    print(f"{female_rate}% of the survivors were female")


# average_age_of_survivors()
# survival_rate()
gender_distribution_of_survivors()
