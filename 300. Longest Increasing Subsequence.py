class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lens = [1] * len(nums)
        
        for i in range(len(nums)):
            candidates = []
            # print(nums[:i])
            for j in range(len(nums[:i])):
                if nums[j] < nums[i]:
                    # print(nums[j], nums[i])
                    candidates.append(j)
            current_max_len = max_lens[i]
            # print(candidates)
            # print('----')
            for candidate in candidates:
                current_max_len = max(current_max_len, max_lens[candidate] + 1)
            max_lens[i] = current_max_len

        # print(max_lens)
        return max(max_lens)