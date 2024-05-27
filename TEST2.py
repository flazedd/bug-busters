import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Sample data
data = np.random.normal(loc=0, scale=1, size=6)  # Replace this with your data
print(data)
print(type(data))
# Visual Inspection
# Histogram
plt.figure(figsize=(12, 6))
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')

# Overlay the normal distribution
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, np.mean(data), np.std(data))
plt.plot(x, p, 'k', linewidth=2)
plt.title('Histogram and Normal Distribution')
plt.show()

# Q-Q Plot
plt.figure(figsize=(6, 6))
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.show()

# Statistical Tests
# Shapiro-Wilk Test
shapiro_stat, shapiro_p = stats.shapiro(data)
print(f"Shapiro-Wilk Test: Statistics={shapiro_stat}, p-value={shapiro_p}")

# Kolmogorov-Smirnov Test
ks_stat, ks_p = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data)))
print(f"Kolmogorov-Smirnov Test: Statistics={ks_stat}, p-value={ks_p}")

# Anderson-Darling Test
ad_stat, _, _ = stats.anderson(data, dist='norm')
print(f"Anderson-Darling Test: Statistics={ad_stat}")

# Interpretation
alpha = 0.05
if shapiro_p > alpha and ks_p > alpha and ad_stat < stats.anderson(data, dist='norm').critical_values[2]:
    print("Data is normally distributed (Fail to reject H0)")
else:
    print("Data is not normally distributed (Reject H0)")
