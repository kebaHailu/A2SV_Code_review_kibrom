class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)


        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j:
                    if isConnected[i][j] != 0:

                        a = j+1
                        b = i+1
                        graph[a].append(b)
                        

        visited = set()

        def dfs(node):

            visited.add(node)

            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb)
            
        count = 0
        for node in range(1,len(isConnected)+1):
            if node not  in visited:
                dfs(node)
                count += 1 
        return count