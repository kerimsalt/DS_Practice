import pandas as pd

df = pd.read_csv("Yahoo finance dataset.csv")
# Data cleaning


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


remove_low_variance_columns(df, 0.01)
