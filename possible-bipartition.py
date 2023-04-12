class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for a , b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        print(graph)
        colored = [0]*n
        visited =set()
        def dfs(node,color):
            
            visited.add(node)
            colored[node-1] = color 
            
            
            for nb in graph[node]:
                if colored[nb-1] != 0:
                    if colored[nb-1] == color:
                        return False 
                    
                if nb not in visited and not dfs(nb,-color):
                    return False
            
            return True 
        
        for i in range(1,n+1):
            if colored[i-1]==0:
                if not dfs(i,1):
                    return False 
            
        return True