class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)

        
        ans =0

        for i in graph:
            for key,val in graph.items():
                if i != key:
                    if i in val:
                        cur = len(graph[i])+len(graph[key])-1
                        
                    else:
                        cur = len(graph[i])+len(graph[key])
                    
                    ans = max(ans,cur)

        return ans