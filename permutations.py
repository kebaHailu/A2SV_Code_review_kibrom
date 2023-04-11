class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        arr = [] # this will return the answer after adding all permutaions 
        mask = 0  
        def backtrack(collect):
            nonlocal mask 
            if len(collect) == len(nums):
                arr.append(collect.copy())
                return 

            
            for i in range(len(nums)):

                if (mask >> i) & 1 == 0:

                    mask |= 1 << i 
                    backtrack(collect+[nums[i]])
                    mask ^= 1 << i
                
        
        backtrack([])
        return arr