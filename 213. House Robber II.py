def rob_partial(nums: List[int]) -> int:
    states = []
    for i in range(len(nums)):
        if i <= 1:
            states.append(nums[i])
            continue
        state = max(states[:i-1]) + nums[i]
        states.append(state)
    return max(states)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(rob_partial(nums[:-1]), rob_partial(nums[1:]))
