"""
Demonstrates imports from a custom package and integration with NumPy.
"""

import numpy as np
from my_package import calculate_mean, filter_above_threshold

def main() -> None:
    data = [12.5, 45.0, 78.2, 23.4, 89.1, 56.3]

    # Custom Module Usage
    mean_val = calculate_mean(data)
    filtered_val = filter_above_threshold(data, 50.0)

    print("==========================================")
    print("        CUSTOM MODULE DEMONSTRATION       ")
    print("==========================================")
    print(f"Original Data  : {data}")
    print(f"Calculated Mean: {mean_val:.2f}")
    print(f"Values > 50    : {filtered_val}")

    # Third-Party Package (NumPy) Usage
    print("\n==========================================")
    print("      THIRD-PARTY PACKAGE (NUMPY) DEMO    ")
    print("==========================================")
    np_array = np.array(data)
    print(f"NumPy Standard Deviation : {np.std(np_array):.2f}")
    print(f"NumPy Normalized (0-1)   : {np.round((np_array - np.min(np_array)) / (np.max(np_array) - np.min(np_array)), 2)}")

if __name__ == "__main__":
    main()