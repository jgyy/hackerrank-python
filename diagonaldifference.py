import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n - 1 - i]
    
    return abs(primary_diagonal_sum - secondary_diagonal_sum)


if __name__ == '__main__':
    result = diagonalDifference([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(result)
