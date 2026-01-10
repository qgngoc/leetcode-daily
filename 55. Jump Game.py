from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        stack = [0]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node >= n-1:
                return True
            for i in range(nums[node]+1):
                stack.append(node+i)

        return False