class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0]) # get the number of rows and columns
        dp = [[0] * cols for _ in range(rows)] # initialize the dp array
        def dfs(r, c, prev): # dfs function to find the longest increasing path
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev:
                return 0 # if the current cell is out of bounds or the current cell is less than or equal to the previous cell, return 0
            if dp[r][c]:
                return dp[r][c] # if the current cell is already visited, return the value of the current cell
            path = 1 # initialize the path length
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                path = max(path, 1 + dfs(r + dr, c + dc, matrix[r][c])) # find the longest increasing path by moving in the four directions
            dp[r][c] = path # update the dp array
            return path # return the path length
        return max(dfs(r, c, float('-inf')) for r in range(rows) for c in range(cols)) # find the longest increasing path by calling the dfs function for each cell