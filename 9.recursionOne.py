# recrusion explanation youtube video

class RecursionGoodLuck:
    # kind of like a compilation of functions
    def __init__(self) -> None:
        pass


    @staticmethod
    def summation(n: int) -> int:
        # base case -- done -> return something and go back to the function
        if (n<=0): 
            return 0
        # keep going
        else: 
            return n + RecursionGoodLuck.summation(n-1)


    @staticmethod
    def factorial(n: int) -> int:
        if (n<=1):
            return 1
        else:
            return n * RecursionGoodLuck.factorial(n-1)


    @staticmethod
    def exponentiation(n: int, exp: int) -> int:
        if (exp <=0):
            return 1
        else:
            return n * RecursionGoodLuck.exponentiation(n,exp-1)


    @staticmethod
    def main(n: int) -> int:
        return (RecursionGoodLuck.summation(n),RecursionGoodLuck.factorial(n), RecursionGoodLuck.exponentiation(n))


if __name__ == "__main__":
    # n = int(input())
    n = 2
    print(RecursionGoodLuck.main(n))


