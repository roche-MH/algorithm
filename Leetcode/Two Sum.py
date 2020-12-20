class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start,end = 0,0
        while True:
            end+=1
            if nums[start]+nums[end] == target:
                return [start,end]
            if end == len(nums)-1:
                start+=1
                end = start
            
