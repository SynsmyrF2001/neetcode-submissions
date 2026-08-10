class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows, cols = len(s), len(t) # get the number of rows and columns
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows + 1): # initialize the dp array
            dp[r][0] = 1 # initialize the first column
        for c in range(1, cols + 1): # initialize the first row
            dp[0][c] = 0 # initialize the first row
        for r in range(1, rows + 1): # fill the dp array
            for c in range(1, cols + 1): # fill the dp array
                if s[r - 1] == t[c - 1]: # if the characters are the same
                    dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c]  # use match + skip
                else: # if the characters are not the same
                    dp[r][c] = dp[r - 1][c]  # skip current char in s
        return dp[-1][-1] # return the last element of the dp array