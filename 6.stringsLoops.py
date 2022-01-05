# Enter your code here. Read input from STDIN. Print output to STDOUT

def stringPartitioning(testsCases: int):
    for i in range(testsCases):
        myString = input()
        evens = [x for x in myString if myString.index(x) % 2 == 0]
        odds = [x for x in myString if myString.index(x) % 2 != 0]
        print("".join(evens), "".join(odds))    

if __name__ == "__main__":
    n = int(input())
    stringPartitioning(n)