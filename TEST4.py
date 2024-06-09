from scipy.stats import wilcoxon
from utility import utils

# Create two lists with the integer 100 six times each
list1 = [100] * 6
list2 = [100] * 6

list1, list2 = utils.adjust_for_zero_differences(list1, list2)
# Perform the Wilcoxon signed-rank test
print(list1, list2)
statistic, p_value = wilcoxon(list1, list2)

# Print the p-value
print("Wilcoxon Test p-value:", p_value)
