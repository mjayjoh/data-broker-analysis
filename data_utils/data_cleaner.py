import pandas as pd
import re
from pathlib import Path

# --- HELPER FUNCTIONS ---
def initial_clean_and_one_hot(data: pd.DataFrame) -> pd.DataFrame:
    """
    Drops duplicates, rows with no 'Collects' data, 
    and one-hot encodes 'RegistrySource'.
    """
    df_cleaned = data.drop_duplicates()
    # Drop rows where all 'Collects' columns are empty
    collects_cols = [col for col in df_cleaned.columns if col.startswith('Collects')]
    mask_to_drop = df_cleaned[collects_cols].isna().all(axis=1)
    df_cleaned = df_cleaned[~mask_to_drop].copy()

    # One-hot encode the RegistrySource for later merging
    df_final = pd.get_dummies(df_cleaned, columns=['RegistrySource'])

    return df_final


def merge_by_normalized_name(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes company names and merges records, combining 
    data sources and collected data types.
    """
    def normalize_name(name):
        if not isinstance(name, str):
            return ""
        name = name.upper()
        name = re.sub(r'\b(INC|LLC|CORPORATION)\b', '', name)  # remove suffixes
        name = re.sub(r'[^\w\s]', '', name)  # remove punctuation
        name = re.sub(r'\s+', ' ', name).strip()  # remove whitespace
        return name

    data['Name'] = data['Name'].apply(normalize_name)
    merge_key = ['Name']
    one_hot_cols = [col for col in data.columns if col.startswith('RegistrySource_')]
    collects_cols = [col for col in data.columns if col.startswith('Collects')]
    other_cols = data.columns.difference(merge_key + one_hot_cols + collects_cols).to_list()
    # 'any': For one-hot cols, if *any* merged row was True, the result is True.
    # 'max': For 'Collects' cols, '1' (Yes) will win over '0' (No) or NaN.
    # 'first': For other cols (like UUID), we just take the first one.
    merged_dict = {
        **{col: 'any' for col in one_hot_cols},
        **{col: 'max' for col in collects_cols},
        **{col: 'first' for col in other_cols}
    }
    data[collects_cols] = data[collects_cols].fillna(0)
    return data.groupby(merge_key, as_index=False).agg(merged_dict)

# --- MAIN FUNCTION ---
def clean_data(input_file_path: str) -> pd.DataFrame:
    """
    Main pipeline function to load, clean, and merge data broker data.
    """
    try:
        data = pd.read_excel(input_file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {input_file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return pd.DataFrame()
    
    df_cleaned = initial_clean_and_one_hot(data)
    result_df = merge_by_normalized_name(df_cleaned)
    output_path = Path("../data/cleaned_data/uq-data-brokers.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(output_path, index=False)
    print(f"File saved to {output_path}")
    return result_df


if __name__ == '__main__':
     raw_file = '../data/raw_data/Data_Broker_Full_Registry_2025.xlsx'
     cleaned_df = clean_data(raw_file)
     print(cleaned_df.head())