import pandas as pd
import argparse
import sys

def sum_columns(csv_file, columns_to_sum, output_file):
    try:
        df = pd.read_csv(csv_file)
        result = df[columns_to_sum].sum()

        print(f"Sum of columns {columns_to_sum}:")
        print(result)

        result.to_csv(output_file, header=True, index=False)
        print(f"Sum result saved to {output_file}")

        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sum specified columns in a CSV file")
    
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("columns_to_sum", help="Columns to sum, separated by commas")
    parser.add_argument("-o", "--output_file", default="../test/csv_sum.data1.out", help="Path to the output CSV file")

    args = parser.parse_args()

    sum_columns(args.csv_file, args.columns_to_sum.split(","), args.output_file)
