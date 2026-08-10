class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): # if the length of s1 and s2 is not equal to the length of s3, return False
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)] # initialize the dp array
        dp[0][0] = True # initialize the starting point
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1] # if the character in s1 is equal to the character in s3, set dp[i][0] to True
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1] # if the character in s2 is equal to the character in s3, set dp[0][j] to True
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) # if the character in s1 is equal to the character in s3, set dp[i][j] to True
        return dp[-1][-1] # return the last element of the dp array