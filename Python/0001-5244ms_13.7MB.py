# Asling-20190514
# best RT: 5244 ms, faster than 21.66%
#      MU: 13.7 MB, less than 33.49%

'''
0001:Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# 暴力循环 [5244ms & 13.7MB]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    a=[i,j]
                    return a
                else:
                    continue