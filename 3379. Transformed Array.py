class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            results.append(nums[(i+nums[i])%len(nums)])
        return results