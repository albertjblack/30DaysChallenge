#!/bin/python3

import math
import os
import random
import re
import sys

class Solution(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def getBinary(n: int)-> int:
        if n:
            remainders = []
            while n >= 1:
                remainders.append(f"{n-(n//2)*2}")
                n //= 2
            return "".join(remainders)
        else:
            return 0

    @staticmethod
    def findConsecutives(n: int) -> int:
        if n:
            n_bin = Solution.getBinary(n)
            _temp = [len(x) for x in n_bin.split('0')]
            max_consecutive_ones = max(_temp)
            return int(max_consecutive_ones)
        else:
            return 0


if __name__ == '__main__':
    n = int(input().strip())
    print(Solution.findConsecutives(n))