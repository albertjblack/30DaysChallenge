#!/bin/python3

import math
import os
import random
import re
import sys

# database #
# Emails #
# FirstName # # EmailID

"""BASED ON 'N' TIMES PRINT EVERY firstname FIELD THAT ITS EMAIL ENDS IN @gmail.com"""

class Solution(object):
    def __init__(self) -> None:
        self.db = []


    def is_gmail(self,email: str):
        pattern = r"[a-z]+.*[a-x]+@gmail.com"
        matches = re.match(pattern=pattern,string=email)
        if matches: return matches.string


    def get_entry_gmail(self, entry):
        if self.is_gmail(entry[1]) != None:
            return entry[0]


if __name__ == '__main__':
    s = Solution()
    arr = []


    """"""
    with open("27.csv", "r") as file:
        f = file.readlines()
        n = int(f[0])
        content = [x.strip().split() for x in f[1:]]

        for entry in content:
            _ = s.get_entry_gmail(entry)
            if _:
                arr.append(_)

    """"""
    
    
    arr.sort(key=lambda x:x)

    for x in arr:
        print(x)
        