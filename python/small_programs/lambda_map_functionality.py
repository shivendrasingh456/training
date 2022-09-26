def filter_divi_by2(x):
	if x%2==0:return True
	else: return False

def map_divi_by2(x):
	if x%2==0:return x

num1=[1,2,3,4,5]
print(f"testing filter function : {list(filter(filter_divi_by2,num1))}")
print(f"testing map function : {list(map(map_divi_by2,num1))}")
