import sys

class Solution:
    # Write your code here
    queue = []
    stack = []
    def __init__(self) -> None:
        pass
    
    # stack
    def pushCharacter(self, char: str):
        self.stack.append(char)

    # dequeue
    def enqueueCharacter(self, char: str):
        self.queue.append(char)
    
    # stack
    def popCharacter(self):
        _ = self.stack.pop(-1)
        return _

    # dequeue
    def dequeueCharacter(self):
        _ = self.queue.pop(0)
        return _

        
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
