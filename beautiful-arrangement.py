class Solution:
    def countArrangement(self, n: int) -> int:
        arr = [i for i in range(1,n+1)]

        ans = 0
        def backtrack(path):
            # print(path)
            nonlocal ans
            if len(path) == len(arr):
                ans += 1
                return 
            
            for i in range(n):

                if (not i+1 in path) and (not (len(path) + 1)%(i+1) or not (i+1)%(len(path) + 1)):
                    path.add(i + 1)
                    backtrack(path)
                    path.remove(i + 1)

        backtrack(set())
        return ans