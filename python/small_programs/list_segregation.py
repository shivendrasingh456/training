#Write a Python program to find list integers containing exactly four distinct values,
#such that no integer repeats twice consecutively among the first twenty entries

def list_checker(stack):
	if len(set(stack))!=4:return False
	length=len(stack)
	for char in range(0,length-1 if length<20 else 19,1):
		if stack[char]==stack[char+1]:return False
	return True

def list_checker2(stack):
    length=len(stack)
    return all(stack[num]!=stack[num+1] for num in range(length-1 if length<20 else 19)) and len(set(stack))==4

if __name__=="__main__":
	try:
		inp=[1,2,4,3,2,1,2,3,4,1,2,3,4,1,2,3,4,1,3,3,3,3,3]
		if len(inp)==0:raise Exception(f"no input")
		print(f"is valid list: {list_checker(inp)}")
	except Exception as e1 :
		raise e1


