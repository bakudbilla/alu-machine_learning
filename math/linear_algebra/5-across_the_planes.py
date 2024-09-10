#!/usr/bin/env python3
"""function to add 2D matrix into a new one"""



def add_matrices2D(mat1, mat2):
     """ adding two matrix element wise

    Args:
        mat1, mat2: Given matrix

    Return:
        the sum of matrix: new matrix

    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    
    # Create a new matrix by adding corresponding elements
    result = []
    for row1, row2 in zip(mat1, mat2):
        new_row = [x + y for x, y in zip(row1, row2)]
        result.append(new_row)
