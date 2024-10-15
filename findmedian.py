import math
import os
import random
import re
import sys

def findMedian(arr):
    n = len(arr)
    arr.sort()
    return arr[n // 2]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(findMedian(arr))
