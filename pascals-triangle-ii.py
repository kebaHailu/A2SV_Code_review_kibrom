class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        num = [0,1,0]
        def passcal(rowIndex, nums):
            if rowIndex == 0:
                return nums
            temp = [0] 

            for i in range(1,len(nums)):
                temp.append(nums[i] + nums[i-1])

            nums = temp[:]
            nums.append(0)

            return passcal(rowIndex - 1, nums)

        return passcal(rowIndex, num)[1:-1]