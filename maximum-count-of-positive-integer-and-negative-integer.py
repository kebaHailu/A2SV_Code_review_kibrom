class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count1= 0
        count2 = 0

        for i in nums:
            if i > 0:
                count1 += 1
            elif i < 0:
                count2 += 1
        
        return max(count1,count2)