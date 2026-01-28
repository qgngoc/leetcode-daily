class Solution:
    def numDecodings(self, s: str) -> int:
        wordDict = {str(i): chr(64 + i) for i in range(1, 27)}
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if i == 0:
                if s[i] in wordDict:
                    dp[i] += 1
                continue

            if s[i] in wordDict and s[i-1] + s[i] in wordDict:
                if i - 2 < 0 or s[i-1] == '0':
                    dp[i] = dp[i-1] + 1
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            elif s[i] == '0' and s[i-1] + s[i] in wordDict:
                dp[i] = dp[i-2] if i-2>=0 else 1
            elif s[i-1] + s[i] in wordDict:
                dp[i] = dp[i-1]
            elif s[i] in wordDict:
                if dp[i-1] == 0 and s[i-1] == '0':
                    return 0
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
        return dp[len(s)-1]

        