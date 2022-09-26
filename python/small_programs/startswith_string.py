#Write a Python program to find the strings in a given list, starting with a given prefix.
import re
from collections import deque

#1st program to match first digits
def valid_prefix(prefix,check_list):
	l1=deque()
	for strs in check_list:
		res=re.search(prefix,strs)
		#Returns None if string match does not exists at any point
		if not res:continue
		if res.start()==0:l1.append(strs)
	return l1

#2st program to match first digits
def valid_prefix2(prefix,check_list):
	return list(filter(lambda strs:strs.startswith(prefix), check_list))

#program to match last digits
def valid_prefix3(prefix,check_list):
	return list(filter(lambda strs:strs.endswith(prefix), check_list))

if __name__=="__main__":
	try:
		inp=[("do",(' cat', ' dog', 'shatter', 'donut', 'at', 'todo'))]
		if len(inp)==0:raise Exception(f"no input")
		prefix=inp[0][0]
		check_list=inp[0][1]
		# print(f"list: {valid_prefix2(prefix,check_list)}")
	
	except Exception as e1 :
		raise e1
