import pandas as pd

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.
    """
    if df.empty:
        return df

    # Drop rows missing essential identifiers
    df = df.dropna(subset=['sensor_id', 'timestamp'])

    # Fill missing numeric values with column means
    numeric_cols = ['ph', 'turbidity', 'dissolved_oxygen', 'temperature']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col].fillna(df[col].mean(), inplace=True)

    # Ensure realistic ranges
    df = df[(df['ph'] >= 0) & (df['ph'] <= 14)]
    df = df[df['turbidity'] >= 0]

    df.reset_index(drop=True, inplace=True)
    return df




