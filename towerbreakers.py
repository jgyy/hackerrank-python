import math
import os
import random
import re
import sys

def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1

if __name__ == "__main__":
    print(towerBreakers(1, 2))
