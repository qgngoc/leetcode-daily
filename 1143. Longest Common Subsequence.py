class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for _ in range(len(text1)+1):
            row = []
            for _ in range(len(text2)+1):
                row.append(0)
            dp.append(row)
        max_len = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                max_len = max(dp[i][j], max_len)
        return max_len
        