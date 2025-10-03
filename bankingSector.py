import numpy as np

# 1. 4 branches × 6 months (sample numbers in thousands)
transactions = np.array([
    [120, 150, 130, 140, 160, 155],
    [200, 180, 210, 190, 205, 220],
    [90,  100, 95,  110, 105, 120],
    [175, 165, 185, 195, 180, 170]
])

# 2. Total transactions per branch
totals_per_branch = transactions.sum(axis=1)
print("Totals per branch:", totals_per_branch)

# 3. Branch with highest total transactions
highest_branch = np.argmax(totals_per_branch) + 1  # +1 for human-friendly index
print("Branch with highest total:", highest_branch)

# 4. Average monthly transaction volume across all branches
avg_monthly = transactions.mean()
print("Average monthly volume across all branches:", avg_monthly)

# 5. Reshape 4×6 to 3×8
reshaped = transactions.reshape(3, 8)
print("Reshaped array (3x8):\n", reshaped)
print(
    "Implication: Data order stays row-major but month/branch meaning is lost—"
    "useful only for internal computation, not for direct reporting."
)
