class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        # dp1 represents ways(i + 1), dp2 represents ways(i + 2)
        dp1, dp2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                current = 0
            else:
                current = dp1
                if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                    current += dp2

            dp1, dp2 = current, dp1

        return dp1

 