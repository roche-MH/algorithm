class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, end = 0, len(nums)
        maxScore,score = 0,0
        seen = set()
        lastIndex = 0
        
        while start < end:
            if nums[start] not in seen:
                seen.add(nums[start])
                score +=nums[start]
            else:
                maxScore = max(score, maxScore)
                for i in range(lastIndex, start):
                    if nums[i] == nums[start]:
                        lastIndex = i+1
                        break
                    score -= nums[i]
                    seen.remove(nums[i])
            start+=1
        return max(maxScore,score)
