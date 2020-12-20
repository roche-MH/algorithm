class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if (len(nums) % 2 != 0):
            median = nums[int((len(nums) - 1) // 2)]
            return median

        else:
            median =float( (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2)
            return median        