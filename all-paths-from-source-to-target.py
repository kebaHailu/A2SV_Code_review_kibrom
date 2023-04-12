class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        di = defaultdict(list)

        for idx,val in enumerate(graph):
            di[idx] = val 


        ans = []

        def dfs(idx,path):
            if idx == len(graph)-1:
                ans.append(path)
                return 

            for i in di[idx]:
                dfs(i,path+[i])

        dfs(0,[0])
        return ans