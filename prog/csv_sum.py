import pandas as pd
import argparse

def sum_columns(csv_file, columns_to_sum):
    try:
        df = pd.read_csv(csv_file)
        result = df[columns_to_sum].sum()
        print(f"Sum of columns {columns_to_sum}:")
        print(result)
        output_file = "../test/csv_sum.data1.out"
        result.to_csv(output_file, header=True)
        print(f"Sum result saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sum specified columns in a CSV file")
    
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("columns_to_sum", help="Columns to sum, separated by commas")

    args = parser.parse_args()

    sum_columns(args.csv_file, args.columns_to_sum.split(","))
