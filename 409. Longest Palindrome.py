class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        n_longests = 0
        have_odds = False
        for value in char_count.values():
            if value % 2 == 0:
                n_longests += value
            else:
                n_longests += value - 1
                have_odds = True
                # max_odds = max(max_odds, value)
        if have_odds:
            n_longests += 1
        return n_longests