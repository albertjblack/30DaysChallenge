class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self,n):
        _ = {1,n}
        i = 2
        while i <= n:
            if n%i == 0 and i not in _:
                _.add(i) 
            else:
                i+=1
        return int(sum(_))


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)