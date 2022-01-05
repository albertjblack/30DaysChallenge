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
    def getMaxSum(arr):
        max_sum = -float('inf')
        if arr:
            rowLen = len(arr)
            colLen = len(arr[0])
            if rowLen < 3 or colLen < 3:
                return -1
            for i in range(rowLen-2):
                for j in range(colLen-2):
                    mysum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                    if mysum > max_sum:
                        max_sum = mysum
            return max_sum
        else:
            return 0
                        

if __name__ == "__main__":

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    print(Solution.getMaxSum(arr))
