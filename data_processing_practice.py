import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
# print(df.head())
# print(df.iloc[0, :5])  # Display the first 5 rows and first 5 columns
# Assume that the df is global and already loaded


def average_age_of_survivors():
    survivors = df[df['survived'] == 1]
    # Calculate the average age of survivors
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


def survival_rate_with_respect_to_class():
    print("Survival rate with respect to class")
    # n_total_passengers = len(df)
    # n_total_survivors = len(df[df["survived"] == 1])

    n_first_class = len(df[df["class"] == "First"])
    n_second_class = len(df[df["class"] == "Second"])
    n_third_class = len(df[df['class'] == "Third"])

    n_first_class_survivor = len(df[(df["class"] == "First") &
                                    (df["survived"] == 1)])
    n_second_class_survivor = len(df[(df["class"] == "Second") &
                                     (df["survived"] == 1)])
    n_third_class_survivor = len(df[(df["class"] == "Third") &
                                    (df["survived"] == 1)])

    f_rate = round(n_first_class_survivor / n_first_class * 100, 2)
    s_rate = round(n_second_class_survivor / n_second_class * 100, 2)
    t_rate = round(n_third_class_survivor / n_third_class * 100, 2)
    print(f"First class survival rate: {f_rate}%")
    print(f"Second class survival rate: {s_rate}%")
    print(f"Third class survival rate: {t_rate}%")


def plot_histogram(df, column, bins=30):
    """
    Plots a basic histogram for a given numeric column.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


def plot_boxplot(df, column):
    """
    Plots a basic boxplot for a given numeric column.
    """
    plt.figure(figsize=(4, 6))
    sns.boxplot(y=df[column])
    plt.title(f'Boxplot of {column}')
    plt.ylabel(column)
    plt.show()


# average_age_of_survivors()
# survival_rate()
# gender_distribution_of_survivors()
# print(df.head(n=10))
# print(df.columns.tolist())
# print(df['class'].unique())
survival_rate_with_respect_to_class()
plot_histogram(df, 'age', bins=20)
plot_boxplot(df, 'age')
