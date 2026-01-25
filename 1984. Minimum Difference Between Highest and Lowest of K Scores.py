class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        i = 0
        diffs = []
        while i+k-1 < len(nums):
            diffs.append(nums[i+k-1] - nums[i])
            i += 1
        min_diff = min(diffs)
        return min_diff