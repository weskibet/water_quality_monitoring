from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator
import os

def main():
    print("💧 Water Quality Monitoring System")

    # Step 1 — Load data
    df = load_csv("sensor_data.csv")
    if df.empty:
        print("❌ No data loaded. Exiting...")
        return

    print("\nRaw Data Preview:")
    print(df.head())

    # Step 2 — Clean data
    df_clean = clean_sensor_data(df)
    print("\n🧹 Cleaned Data Preview:")
    print(df_clean.head())

    # Step 3 — Evaluate
    evaluator = WaterQualityEvaluator()
    df_eval = evaluator.evaluate(df_clean)

    # Step 4 — Print results
    print("\n📊 Water Quality Evaluation Results:")
    print(df_eval[['sensor_id', 'timestamp', 'ph', 'turbidity', 'is_water_safe']])

    # Step 5 — Save results to results/ folder
    base_dir = os.path.dirname(os.path.dirname(__file__))
    results_path = os.path.join(base_dir, "results")
    os.makedirs(results_path, exist_ok=True)
    output_file = os.path.join(results_path, "results.csv")
    df_eval.to_csv(output_file, index=False)
    print(f"\n📥 Results saved to {output_file}")

if __name__ == "__main__":
    main()
