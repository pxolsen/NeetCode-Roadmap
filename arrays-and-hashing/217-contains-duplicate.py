# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

######## My Solution ########
def containsDuplicate(nums):
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            return True
    return False








print(containsDuplicate([1,2,3,1])) ## True
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) ## True
print(containsDuplicate([1,2,3,4])) ## False
