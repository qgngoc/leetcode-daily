class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        window_size = 0
        max_window_size = 0
        while i + window_size < len(nums):
            current_min = nums[i]
            current_max = nums[i+window_size]
            if current_min * k >= current_max:
                window_size += 1
            else:
                i += 1
            max_window_size = max(window_size, max_window_size)
        return len(nums) - max_window_size