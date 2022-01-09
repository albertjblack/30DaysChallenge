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
    def bubbleSort(a: list) -> list:
        swaps = 0
        theLength = len(a)
        isSorted = False
        while not isSorted:
            try:
                for i in range(0,theLength-1):
                    if a[i]>a[i+1]:
                        a[i],a[i+1]=a[i+1],a[i]
                        swaps += 1
                theLength -= 1
                if  theLength<=0:
                    isSorted = True
            except Exception as e:
                print(e)
        return (a,swaps)



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    #a = [9,8,4,1,9,8]
    bubbleResults = Solution.bubbleSort(a)
    print(f"Array is sorted in {bubbleResults[1]} swaps.")
    print(f"First Element: {bubbleResults[0][0]}")
    print(f"Last Element: {bubbleResults[0][-1]}")