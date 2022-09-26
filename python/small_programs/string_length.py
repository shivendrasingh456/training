#Q.Write a Python program to find the lengths of a given list of non-empty strings

if __name__=="__main__":
	try:
		inp=['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
		if len(inp)==0:raise Exception(f"no input")
		print(f"string length list : {list(map(lambda x : len(x),inp))}")
	
	except Exception as e1 :
		raise e1

