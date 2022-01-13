
class Solution(object):
    def __init__(self):
        pass

    @staticmethod
    def is_prime(n):
        if n == 1:
            return "Not prime"
        for i in range(2, int( (n**(1/2)) + 1)):
            if n % i == 0:
                return "Not prime"
        return "Prime"


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(Solution.is_prime(n))