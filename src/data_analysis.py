"""
Demonstrates data manipulation using the Pandas library.
"""

import pandas as pd

def analyze_dataset() -> None:
    dataset = {
        "Employee": ["Alice", "Bob", "Charlie", "David"],
        "Department": ["Engineering", "HR", "Engineering", "Marketing"],
        "Salary": [85000, 62000, 92000, 58000]
    }

    df = pd.DataFrame(dataset)
    
    print("==========================================")
    print("      THIRD-PARTY PACKAGE (PANDAS) DEMO   ")
    print("==========================================")
    print("DataFrame View:\n", df)
    print("\nAverage Salary by Department:\n", df.groupby("Department")["Salary"].mean())

if __name__ == "__main__":
    analyze_dataset()