import numpy as np
import scipy.stats as stats

# Sample data
data1 = np.random.normal(loc=0, scale=1, size=1000)  # Replace with your first dataset
data2 = np.random.normal(loc=0, scale=0.9, size=1000)  # Replace with your second dataset

# Levene's Test
levene_stat, levene_p = stats.levene(data1, data2)

# Interpretation
alpha = 0.05
print(f"Levene's Test: Statistics={levene_stat}, p-value={levene_p}")

if levene_p > alpha:
    print("Fail to reject the null hypothesis. The variances are equal.")
else:
    print("Reject the null hypothesis. The variances are not equal.")
