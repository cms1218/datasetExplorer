import dataUtils
import argparse

def practiceExplore():
    parser = argparse.ArgumentParser(description="Explore a CSV dataset.")
    parser.add_argument(
        "--dataset", 
        type=str,
        required=True,
        help="Path to the CSV dataset file."
    )

    args = parser.parse_args()
    df = dataUtils.load_csv(args.dataset)
    dataUtils.missing_values_table(df)
