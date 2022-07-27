#User function Template for python3
from collections import deque
class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        self.string=x
        return self.isBalanced()

    def isBalanced(self):
        mirror_image={'{':'}','[':']','(':')'}
        l1=deque()
        for char in self.string:
            if char in('{','[','('):
                l1.append(mirror_image[char])
            else:
                if len(l1)==0: return False            
                if l1.pop()==char: pass
                else: return False

        return True if len(l1)==0 else False
