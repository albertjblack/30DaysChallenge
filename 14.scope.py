class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    def computeDifference(self):
        __len = len(self.__elements)
        __set = set()
        for i in range(__len):
            for j in range(__len):
                if (i,j) not in __set and (j,i) not in __set:
                    __set.add((i,j))
                    __set.add((j,i))
                    mydiff = abs(self.__elements[i]-self.__elements[j])
                    if mydiff > self.maximumDifference:
                        self.maximumDifference = mydiff
    

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)