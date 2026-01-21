class Solution:
    def rob(self, nums: List[int]) -> int:
        states = []
        for i in range(len(nums)):
            if i <= 1:
                states.append(nums[i])
                continue
            state = max(states[:i-1]) + nums[i]
            states.append(state)
        return max(states)