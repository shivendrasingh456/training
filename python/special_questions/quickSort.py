# Python program for implementation of Quicksort Sort

def partition(l,r,nums):
	pivot,ptr=nums[r],l
	for i in range(l,r):
		if pivot>=nums[i]:
			nums[i],nums[ptr]=nums[ptr],nums[i]
			ptr+=1
	nums[ptr],nums[r]=nums[r],nums[ptr]
	return ptr

def quicksort(l,r,nums):
	if len(nums)==1: #eliminating the extreme condition
		return nums
	else:
		if r>l:
			pi=partition(l,r,nums)
			quicksort(l,pi-1,nums) #Recursively sorting the left values
			quicksort(pi+1,r,nums) #Recursively sorting the right values
	return nums

# inp=[4, 5, 1, 2, 3]
inp=[3,5,2,5,66,7,1,2,2,9,76]
print(f"example : {inp}{quicksort(0, len(inp)-1, inp)}")


