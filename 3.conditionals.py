#!/bin/python3

import math
import os
import random
import re
import sys

class Solution:
    def __init__(self,N):
        self.n = N
    
    def integerThing(self):
        if self.n % 2 == 1:
            print("Weird")
        elif self.n % 2 == 0 and self.n >=2 and self.n <=5:
            print("Not Weird")
        elif self.n % 2 == 0 and self.n >= 6 and self.n <= 20:
            print("Weird")
        elif self.n % 2 == 0 and self.n >20:
            print("Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    mySol = Solution(N)
    mySol.integerThing()