import numpy as np
from scipy.stats import wilcoxon
import warnings

# Function to compute Vargha-Delaney A measure
def vargha_delaney_A(x, y):
    n1 = len(x)
    n2 = len(y)
    combined = np.concatenate([x, y])
    ranks = np.argsort(np.argsort(combined))
    r1 = np.sum(ranks[:n1])
    A = (r1 - n1 * (n1 + 1) / 2) / (n1 * n2)
    return A

# Generate 1000 random samples for two groups
np.random.seed(42)  # For reproducibility
sn = 1
x = np.random.normal(loc=0, scale=1, size=sn)
y = np.random.normal(loc=1, scale=1, size=sn)


w_stat, p_value = wilcoxon(x, y)

# Calculate Vargha-Delaney A measure
A = vargha_delaney_A(x, y)

print(f"Wilcoxon signed-rank test statistic: {w_stat}")
print(f"P-value: {p_value}")
print(f"Vargha-Delaney A measure: {A}")
