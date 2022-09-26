#Python program for calculating no of character count

from collections import deque
from collections import Counter

def repeat_string(hash):
	return "".join(str(key)+str(value) for key,value in hash.items())

def repeat_string2(inp):
	hash={}
	for char in inp:
		if char in hash.keys():hash[char]+=1
		else:hash[char]=1
	return "".join(str(key)+str(value) for key,value in hash.items())

def repeat_string3(strs):
	lst=set(strs)
	return "".join(char+str(strs.count(char))for char in lst)

if __name__=="__main__":
	try:
		inp='aaaabbbbcccccfff'
		inp=inp.strip()
		if len(inp)==0:raise Exception(f"input is null")
		hash=Counter(inp)
		print(f"string with count: {repeat_string(hash)}")

	except Exception as e1:
		raise e1

