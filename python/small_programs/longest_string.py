# Write a Python program find the longest string of a given list of strings

#1st function to find maximum in list
def is_max(lst):
	string_max=''
	for n in range(0,len(lst)):
		if len(string_max)<len(lst[n]):string_max=lst[n]
	return string_max

#2nd function to find maximum in list
def is_max2(lst):
	hash={len(x):x for x in lst}
	return hash[max(hash)]

if __name__=="__main__":
	try:
		inp=['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
		if len(inp)==0:raise Exception(f"input is null")
		print(f"String having maximum length is {is_max(inp)}")
		
	except Exception as e1:
		raise e1

