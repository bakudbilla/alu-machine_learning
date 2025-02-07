#!/usr/bin/env python3
"""Script for early stopping regularization algorithm"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """
    Function of early stopping

    """
    if opt_cost - cost > threshold:
        count = 0
    else:
        count += 1
    if count != patience:
        return False, count
    else:
        return True, count
