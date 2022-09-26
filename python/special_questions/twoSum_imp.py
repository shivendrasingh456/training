# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    nums_dict={}
    for i in range(len(nums)):
        if (target-nums[i]) in nums_dict.keys():
            return [nums_dict[target-nums[i]],i]
        nums_dict[nums[i]]=i

if __name__=="__main__":
    try:
        nums=[0,0]   
        target=0
        print(f"Integer having {target} is {twoSum(nums,target)}")
    except Exception as e1:
        raise e1


