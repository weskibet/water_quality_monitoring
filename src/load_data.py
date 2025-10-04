import pandas as pd
import os

def load_csv(filename: str) -> pd.DataFrame:
    """
    Load CSV from data/ folder and normalize headers.
    """
    try:
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one folder
        full_path = os.path.join(base_dir, "data", filename)

        df = pd.read_csv(full_path)

        # Normalize headers: remove whitespace & lowercase names
        df.columns = df.columns.str.strip().str.lower()

        print(f"✅ Successfully loaded data from {full_path}")
        print(f"Columns found: {df.columns.tolist()}")  # Debugging
        return df

    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return pd.DataFrame()
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()

