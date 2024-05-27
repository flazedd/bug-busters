from scipy import stats

# Assuming you have two samples or arrays: sample1 and sample2
# Example data
sample1 = [1, 2, 3, 4, 5]
sample2 = [6, 7, 8, 9, 10]

# Perform t-test
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

# Print the results
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the means of the two samples.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the means of the two samples.")
