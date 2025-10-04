import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        ph_safe = self.ph_range[0] <= row["ph"] <= self.ph_range[1]
        turbidity_safe = row["turbidity"] <= self.turbidity_threshold
        return ph_safe and turbidity_safe

    def evaluate(self, df: pd.DataFrame) -> pd.DataFrame:
        df["is_water_safe"] = df.apply(self.is_safe, axis=1)
        return df
