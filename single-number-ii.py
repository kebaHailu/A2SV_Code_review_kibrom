class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        def x3or(a,b,c):
                return ~a&b&c | a&~b&~c , a&b&c | ~a&~b&c | ~a&b&~c 
            
        x = y = 0 
        
        for z in nums:
            x,y=x3or(x,y,z)
        
        return y