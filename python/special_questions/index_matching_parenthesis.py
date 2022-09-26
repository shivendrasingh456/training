# Write a Python program to find the index of the matching parentheses for each character in a given string

from re import I
import sys

def matching_patenthese_version1(strs):
	stack=[]
	strs=strs.strip()
	end=0
	for i in range(1,len(strs)):
		if strs[i-1]+strs[i]==")(":
			for n in range(i-1,end-1,-1):stack.append(n)
			end=i
	for n in range(len(strs),len(stack),-1):stack.append(n)
	return stack

def matching_patenthese_version2(strs):
	stack=list(strs)
	l1=[]
	for n in range(len(strs)):
		if strs[n]=="(":l1.append(n)
		else:
			stack[l1[-1]]=n
			stack[n]=l1.pop()
	return stack

inp="()(())()()()()()((()))"
print(f"length of string : {len(inp)}")
print(f"matching index list : {matching_patenthese_version2(inp)}")

