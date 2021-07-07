#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time complexity: O(mn)
        # Space complexity:O(mn)
        # check if the grid is empty or none
        if not grid: return 0
        # get number of row and columns
        n_row = len(grid)
        n_col = len(grid[0])
        n_islands = 0
        # scan grid map using DFS
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '1':
                    n_islands += 1
                    self.DFS(grid, i, j)
        return n_islands

        
    def DFS(self, grid: List[List[str]], i, j):
        # get number of row and columns
        n_row = len(grid)
        n_col = len(grid[0])
        # if out of bounder or visited cell, then end search
        if i < 0 or i >= n_row or j < 0 or j >= n_col or grid[i][j] == '0': return
        # mark cell is visited as 0
        grid[i][j] = '0'
        # DFS on four direction
        self.DFS(grid, i - 1, j)
        self.DFS(grid, i + 1, j)
        self.DFS(grid, i, j - 1)
        self.DFS(grid, i, j + 1)

# @lc code=end

