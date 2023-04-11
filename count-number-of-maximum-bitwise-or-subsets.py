class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        def max_or(nums):
            val = nums[0]

            for i in nums:
                val |= i
            
            return val
        maxOr = max_or(nums)
        
        arr = []
        for i in range(1,len(nums)+1):
            arr.extend(combinations(nums,i))
     


        for a in arr:
            if maxOr == max_or(a):
                count += 1
        
        return count