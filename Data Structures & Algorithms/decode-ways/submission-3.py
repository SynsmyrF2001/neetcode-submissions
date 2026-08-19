class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # dp[i] will store the number of ways to decode the first i characters
        dp = [0] * (n + 1)

        # Base case: empty string has 1 way to be decoded
        dp[0] = 1

        # dp[1]: ways to decode the first character
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            # Check single digit decoding
            one_digit = int(s[i - 1])
            if one_digit >= 1: # s[i - 1] is not '0
                dp[i] += dp[i - 1]
            
            # Check two digit decoding
            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
        