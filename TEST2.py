def adjust_for_zero_differences(list1, list2, epsilon=1e-10):
    """
    Adjust the elements of list2 by adding a small epsilon value if the difference between corresponding elements of list1 and list2 is zero.

    Parameters:
    list1 (list): The first list of values.
    list2 (list): The second list of values.
    epsilon (float): The small value to add to elements in list2 if the difference is zero (default is 1e-10).

    Returns:
    tuple: Two lists, the original list1 and the adjusted list2.
    """
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

    adjusted_list2 = [
        val2 + epsilon if val1 == val2 else val2
        for val1, val2 in zip(list1, list2)
    ]

    return list1, adjusted_list2


# Example usage
before_treatment = [85, 78, 92, 88, 76, 80]
after_treatment = [88, 79, 94, 91, 77, 80]  # Note the last pair has zero difference

adjusted_before, adjusted_after = adjust_for_zero_differences(before_treatment, after_treatment)

print("Original list:", before_treatment)
print("Adjusted list:", adjusted_after)
