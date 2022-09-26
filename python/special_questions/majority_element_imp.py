#Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.


# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
from collections import Counter

def majority_element_func1(lst) :
    """sdf
    """
    nums_dict={}
    for char in lst:
        if char in nums_dict:
            nums_dict[char]=nums_dict[char]+1
        else:
            nums_dict[char]=1
        if len(lst)//2+1 in nums_dict.values():
            return char
    raise Exception("no majority element")

def majority_element_func2(lst):
    """sdf
    """
    counter=Counter(lst)
    for key,value in counter.items():
        if len(lst)//2<value:
            return key
    raise Exception("no majority element")


if __name__=="__main__":
    try:
        nums = [2,3,3,3,3]
        print(f"{majority_element_func2(nums)}")
    except Exception as e1:
        raise e1
