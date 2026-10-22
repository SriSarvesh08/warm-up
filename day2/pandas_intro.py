from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "students.csv"
OUTPUT_FILE = BASE_DIR / "cleaned_students.csv"


def main():
    try:
        
        df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")

        df.columns = df.columns.str.strip().str.lower()

        required_columns = {"name", "marks"}

        if not required_columns.issubset(df.columns):
            raise ValueError(
                "CSV must contain: name, marks"
            )

        print("\n--- Original Data ---")
        print(df.head())

        # Inspect the dataset
        print("\n--- DataFrame Info ---")
        df.info()

        print("\n--- Statistical Summary ---")
        print(df.describe())

        # Handle missing and invalid values
        df["name"] = df["name"].astype("string").str.strip()
       
        df["name"] = df["name"].replace("", pd.NA)

        df["marks"] = pd.to_numeric(
            df["marks"], errors="coerce"
        )

        # Marks must be between 0 and 100
        df.loc[
            ~df["marks"].between(0, 100), "marks"
        ] = pd.NA

        # Replace missing names
        df["name"] = df["name"].fillna("Unknown")
    
        # Fill missing marks using the median
        median_marks = df["marks"].median()

        if pd.isna(median_marks):
            print("Error: No valid marks available to clean the data.")
            return

        df["marks"] = df["marks"].fillna(median_marks)

        print("\n--- Missing Values After Cleaning ---")
        print(df.isnull().sum())

        # 4. Filter students scoring 80 or above
        high_scorers = df[df["marks"] >= 80]

        print("\n--- Students Scoring 80 or Above ---")
        print(high_scorers)

        # 5. Create a result column for grouping
        df["result"] = df["marks"].apply(
            lambda marks: "Pass" if marks >= 40 else "Fail"
        )

        # 6. Group and aggregate
        summary = df.groupby("result").agg(
            student_count=("name", "count"),
            average_marks=("marks", "mean"),
            highest_marks=("marks", "max"),
            lowest_marks=("marks", "min")
        )

        print("\n--- Grouped Summary ---")
        print(summary)

        # 7. Save the cleaned dataset
        df.to_csv(OUTPUT_FILE, index=False)

        print(f"\nCleaned CSV saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: Input CSV not found: {INPUT_FILE}")

    except pd.errors.EmptyDataError:
        print("Error: The input CSV file is empty.")

    except (ValueError, pd.errors.ParserError) as error:
        print(f"Error processing CSV: {error}")


if __name__ == "__main__":
    main()
