

def encode(s: str, letter: str) -> list:
    encoded = []
    for char in s:
        if char == letter:
            encoded.append(1)
        else:
            encoded.append(0)
    return encoded

def longest_subarray(nums: list, k: int) -> int:
    left = 0
    right = 0
    n_zeros = 0
    max_len = 0
    while right < len(nums):
        if nums[right] == 0:
            n_zeros += 1
        
        while n_zeros > k and left < len(nums):
            if nums[left] == 0:
                n_zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        max_len = 0
        for letter in uppercase_letters:
            encoded_s = encode(s, letter)
            max_len = max(max_len, longest_subarray(encoded_s, k))
        return max_len