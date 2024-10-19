import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    miniMaxSum([0, 1, 2, 3, 4])
