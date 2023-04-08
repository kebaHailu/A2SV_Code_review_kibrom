class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def inbound(row,col):
            return (0<=row<len(image) and 0<=col<len(image[0]))

        start = image[sr][sc]
        def dfs(grid,visited,row,col):
            nonlocal start
            if not inbound(row,col) or grid[row][col] != start:
                return 
            
            visited.add((row,col))
            grid[row][col] = color 


            for cur_row, cur_col in directions:
                new_row = row + cur_row
                new_col = col + cur_col 

                if not (new_row,new_col) in visited:
                    dfs(grid,visited,new_row,new_col)
            
            return 
        
        dfs(image,set(),sr,sc)
        return image