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
    def stringToInteger(S):
        try:
            return int(S)
        except Exception as e:
            return "Bad String"


S = input().strip()
print(Solution.stringToInteger(S))