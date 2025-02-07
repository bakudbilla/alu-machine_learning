#!/usr/bin/env python3
"""Script to use L2 regularization in a DNN"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    Fucntion to implement L2 regularization

    """
    norm = 0
    for key, values in weights.items():
        if key[0] == 'W':
            norm = norm + np.linalg.norm(values)
    L2_cost = cost + (lambtha / (2 * m) * norm)
    return L2_cost
