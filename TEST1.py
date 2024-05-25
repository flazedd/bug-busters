# from scipy import stats
#
# # Define two lists of numbers
# group1 = [10, 12, 14, 15, 16, 18]
# group2 = [13, 15, 16, 17, 19, 20]
#
# # Perform independent samples t-test
# t_statistic, p_value = stats.ttest_ind(group1, group2)
#
# # Print the results
# print("t-statistic:", t_statistic)
# print("p-value:", p_value)
#
# # Define two lists of numbers
# group1 = [10, 12, 14, 15, 16, 18]
# group2 = [13, 15, 16, 17, 19, 20]
#
# # Perform Mann-Whitney U test
# u_statistic, p_value = stats.mannwhitneyu(group1, group2)
#
# # Print the results
# print("U statistic:", u_statistic)
# print("p-value:", p_value)

# # Example lists of lists
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# list2 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
#
# # Zip the two lists together
# zipped_lists = list(zip(list1, list2))
#
# # Print the result
# print(zipped_lists)
import pandas as pd
import numpy as np
import matplotlib as mpl

# Create the DataFrame
df = pd.DataFrame({
    "strings": ["Adam", "Mike"],
    "ints": [1, 3],
    "floats": [1.123, 1000.23]
})

# Style the DataFrame
styled_df = df.style \
  .format({"floats": "{:,.3f}"}) \
  .format_index(str.upper, axis=1) \
  .set_caption("Styled DataFrame Example")

# Rename the index
df.index = ["row 1", "row 2"]

# To display the styled DataFrame in a Jupyter Notebook
print(styled_df)


