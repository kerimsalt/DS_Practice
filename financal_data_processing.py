import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

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


def remove_highly_correlated_features(df, threshold=0.9):
    """
    Removes one of each pair of features with absolute Pearson correlation
    above the threshold. This is useful for reducing multicollinearity
    in the dataset.
    Parameters:
    - df: pandas DataFrame
    - threshold: float, correlation coefficient threshold for dropping one of
    the features

    Returns:
    - A new DataFrame with reduced multicollinearity
    """
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    corr_matrix = df_numeric.corr().abs()
    upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    # Find features with high correlation
    to_drop = [column for column in upper_triangle.columns
               if any(upper_triangle[column] > threshold)]

    print(f"Columns dropped due to correlation > {threshold}: {to_drop}")
    return df.drop(columns=to_drop)


def histogram_boxplot(df, feature):
    # Set plot style
    df = z_score_normalization(df)

    sns.set_theme(style="whitegrid")

    # Create a figure with 2 subplots: histogram + boxplot
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    # Histogram
    sns.histplot(df[feature], bins=10, kde=False, ax=axs[0])
    axs[0].set_title(f'Histogram of {feature}')
    axs[0].set_xlabel(feature)
    axs[0].set_xlim(0, 1000)  # Adjust this based on your dataset

    # Boxplot
    sns.boxplot(y=df[feature], ax=axs[1])
    axs[1].set_title(f'Boxplot of {feature}')
    axs[1].set_ylim(0, 1000)

    plt.tight_layout()
    plt.show()


def top_correlated_features(df, top_n=3):
    # Keep only numeric features
    df_numeric = df.select_dtypes(include=['float64', 'int64'])

    # Compute correlation matrix
    corr_matrix = df_numeric.corr()

    # Mask the lower triangle and diagonal
    mask = np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    corr_vals = corr_matrix.where(mask)

    # Unstack and sort the correlation values
    sorted_pairs = corr_vals.unstack().dropna().sort_values(ascending=False)

    # Print top N correlated feature pairs
    print(f"\nTop {top_n} most strongly correlated feature pairs:")
    for (f1, f2), corr_value in sorted_pairs.head(top_n).items():
        print(f"{f1} & {f2} → correlation: {corr_value:.3f}")


def remove_highly_correlated_features(df, threshold=0.9):
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    corr_matrix = df_numeric.corr().abs()

    # Get upper triangle mask (excluding self-correlation)
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    # Identify columns to drop
    to_drop = [col for col in upper.columns if any(upper[col] > threshold)]

    print(f"Dropping {len(to_drop)} highly correlated features: {to_drop}")
    return df.drop(columns=to_drop)


def remove_outliers_by_zscore(df, threshold=3):
    df_numeric = df.select_dtypes(include=['float64', 'int64'])

    # Compute Z-scores and filter
    z_scores = np.abs(zscore(df_numeric, nan_policy='omit'))
    mask = (z_scores < threshold).all(axis=1)

    print(f"Removed {len(df) - mask.sum()} rows as outliers (Z > {threshold})")
    return df[mask]


def grouped_summary_by_risk(df, group_col='risk_score_text', price_col='previous_close', name_col='company'):
    """
    Groups dataset by a qualitative risk category and computes:
    - Mean previous_close price
    - Company count
    - List of company names

    Parameters:
        df: pandas DataFrame
        group_col: the column to group by
        price_col: column to compute mean (e.g., 'previous_close')
        name_col: column with company name (e.g., 'url' or inferred)

    Returns:
        summary_df: aggregated summary
    """
    if name_col not in df.columns:
        df[name_col] = df['url']  # fallback to URL as company identifier

    grouped = df.groupby(group_col).agg(
        mean_closing_price=(price_col, 'mean'),
        company_count=(name_col, 'count'),
        company_names=(name_col, lambda x: list(x))
    ).sort_values('mean_closing_price', ascending=False)

    return grouped


print("remove low variance")
remove_low_variance_columns(df, 0.01)
print("z-score normalization")
z_score_normalization(df)
print("min max normalization")
min_max_normalization(df)
print("remove highly correlated columns/features")
remove_highly_correlated_features(df, 0.95)
print("Stats")
print(df["closing_price"].mean())
print(df["closing_price"].median())
print(df["closing_price"].std())
print(df["closing_price"].var())
print(df["closing_price"].min())
print(df["closing_price"].max())

# histogram_boxplot(df, "closing_price")
top_correlated_features(df, 3)

# Preprosessing the data
remove_highly_correlated_features(df, 0.9)

remove_outliers_by_zscore(df, 3)
print(df.columns)
grouped_summary_by_risk(df)
