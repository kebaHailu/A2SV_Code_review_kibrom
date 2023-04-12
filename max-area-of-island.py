class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        def inbound(row,col):
            return (0<= row < len(grid) and 0 <= col < len(grid[0]))
        
        visited = set()
        def dfs(row,col):
            if not inbound(row,col) or (row,col) in visited or not grid[row][col]:
                return 0
          
            visited.add((row,col))
            count = 0
            for new_row , new_col in directions:
                new_row = new_row + row 
                new_col = new_col + col 

                count += dfs(new_row,new_col)

            
            return count+1
        
        max_ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_ans = max(max_ans,dfs(i,j))
        
        return max_ans