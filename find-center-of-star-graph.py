class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        a = edges[0]
        b = edges[1]

        return a[0] if a[0] in b else a[1]