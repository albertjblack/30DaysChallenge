
from os import stat

class NegativeNumberException(Exception):
    def __init__(self, message="n and p should be non-negative"):
        self.message = message


    def __str__(self) -> str:
        return(f"{self.message}")


class Calculator(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def power(n,p):
        if n <0 or p<0:
            raise NegativeNumberException
        else:
            return int(n)**int(p)

calc = Calculator()
n,p = 0,-1
try:
    print(calc.power(n,p))
except NegativeNumberException as e:
    print(e)
    
""" 
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Ne as e:
        print(e)   
"""
 