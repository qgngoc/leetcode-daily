class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_arr_dict = {0: 1}
        sum_arr = []
        curr_sum = 0
        n = 0
        for i, num in enumerate(nums):
            curr_sum += num
            n += sum_arr_dict.get(curr_sum - k, 0)
            sum_arr_dict[curr_sum] = sum_arr_dict.get(curr_sum, 0) + 1
        return n
