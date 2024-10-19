import math
import os
import random
import re
import sys

def lonelyinteger(a):
    result = 0
    for num in a:
        result ^= num
    return result

if __name__ == '__main__':
    print(lonelyinteger([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
