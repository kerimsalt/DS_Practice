import pandas as pd

df = pd.read_csv("Yahoo finance dataset.csv")
# Data cleaning


def z_score_normalization(df):
    """
    Apply Z-score normalization to numeric columns in the DataFrame.
    Non-numeric columns will be left unchanged.
    """
    print("before")
    print(df["closing_price"])
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    df_scaled = (df_numeric - df_numeric.mean()) / df_numeric.std()
    print("after")
    print(df_scaled["closing_price"])
    # To keep original non-numeric columns:
    return df_scaled.join(df.drop(columns=df_numeric.columns))


def min_max_normalization(df):
    print("before")
    print(df["closing_price"])
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    df_scaled = (df_numeric - df_numeric.min()) / (df_numeric.max() -
                                                   df_numeric.min())
    df_scaled = df_scaled.join(df.drop(columns=df_numeric.columns))
    print("after")
    print(df_scaled["closing_price"])
    return df_scaled


def remove_low_variance_columns(df, threshold=0.01):
    """
    Removes columns from the DataFrame where variance is below the given
    threshold.
    Parameters:
    - df: pandas DataFrame
    - threshold: float, columns with variance below this will be dropped
    Returns:
    - A new DataFrame with low-variance columns removed
    """
    # Select only numeric columns
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    # Identify columns with variance below threshold
    low_variance_cols = df_numeric.var()[df_numeric.var() < threshold].index
    # Print stats
    print("Total number of columns:", len(df.columns))
    print("Number of columns with variance below threshold:",
          len(low_variance_cols))
    # Drop low-variance columns
    return df.drop(columns=low_variance_cols)


print("remove low variance")
remove_low_variance_columns(df, 0.01)
print("z-score normalization")
z_score_normalization(df)
print("min max normalization")
min_max_normalization(df)
