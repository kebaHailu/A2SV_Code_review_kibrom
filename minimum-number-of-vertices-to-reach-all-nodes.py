class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        end = set()
        for a , b in edges:
            graph[a].append(b)
            end.add(b)
        
        ans = []
        for key in graph:
            if key not in end:
                ans.append(key)
        
        return ans