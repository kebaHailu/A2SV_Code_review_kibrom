class Solution:
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def predict(arr,l,r,cond):

            if l == r:
                if cond:
                    return [arr[l], 0]
                
                return [0,arr[r]]

            if cond:
                right = predict(arr,l,r-1,not cond)
                right[0] += arr[r]
                left = predict(arr,l+1,r,not cond)
                left[0] += arr[l]
                if right[0] >= left[0]:
                    return right
                return left 
            else :
                right = predict(arr,l,r-1,not cond)
                right[1] += arr[r]
                left = predict(arr,l+1,r,not cond)
                left[1] += arr[l]
                if right[1] >= left[1]:
                    return right 
                return left

        final = predict(nums,0,len(nums)-1,True)
        return final[0] >= final[1]