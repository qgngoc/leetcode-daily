
def get_min_index(nums):
    min_index = 0
    for i in range(len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i
    return min_index

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        nums.pop(0)
        min_index = get_min_index(nums)
        cost += nums[min_index]
        nums.pop(min_index)
        min_index = get_min_index(nums)
        cost += nums[min_index]
        # nums.pop(min_index)
        return cost
        