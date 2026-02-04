class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        permutated = False
        while i >= 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j > i:
                if nums[i] < nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    break
                j -= 1
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1
        else:
            nums.reverse()