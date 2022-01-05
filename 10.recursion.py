
import math
import os
import random
import re
import sys

class Recursion(object):
    def __init__(self) -> None:
        super().__init__()

    
    @staticmethod
    def Factorial(n: int) -> int:
        if (n<=1):
            return 1
        else:
            return n * Recursion.Factorial(n-1)


if __name__ == '__main__':
    n = int(input())
    print(Recursion.Factorial(n))


