#!/usr/bin/python3
"""Model having pascal triangle"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [1]  # First element is always 1
        if i > 0:  # Starting from the second row
            last_row = triangle[-1]
            for j in range(1, i):
                row.append(last_row[j-1] + last_row[j])
            row.append(1)  # Last element is always 1
        triangle.append(row)
    
    return triangle

