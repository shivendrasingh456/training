list=[1232]
target=123

class Solution:
    def __init__(self,list,target):
        self.target=target
        self.list=list
        self.start=0
        self.end=len(list)-1

    def binarysearch(self):
        while(self.end>=self.start):
            guess=int((self.start+self.end)/2)
            if self.target==self.list[guess]:
                return guess
            else:
                if self.list[guess]>target:
                    self.end=guess-1
                else:
                    self.start= guess+1
        return []
a=Solution(list,target).binarysearch()
print(f"a : {a}")