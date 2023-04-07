class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def inbound(row,col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        


        def dfs(grid,visited,row,col):
            # base case
            if not inbound(row,col) or grid[row][col] == 0 :
                return 1
            visited.add((row,col))
            count = 0
            for cur_row,cur_col in directions:
                new_row = cur_row+row
                new_col = col + cur_col
                if not (new_row,new_col) in visited:
                    count += dfs(grid,visited,new_row,new_col)

            return count 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid,set(),i,j)