from typing import List

import numpy as np
from scipy.stats import rankdata


def vargha_delaney_effect_size(x: List, y: List) -> float:
    """
    Calculate the Vargha-Delaney A effect size.
    """
    m = len(x)
    n = len(y)
    r = rankdata(np.concatenate([x, y]))
    r1 = np.sum(r[:m])
    A = (r1 / m - (m + 1) / 2) / n
    return A


# Example data
group1 = [89995, 9978, 99992, 88999, 999]
group2 = [3, 4, 3, 2, 1]

# Calculate the Vargha-Delaney effect size
A = vargha_delaney_effect_size(group2, group1)

print('Vargha-Delaney A effect size: %.3f' % A)
