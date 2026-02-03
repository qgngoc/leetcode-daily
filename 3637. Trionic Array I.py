class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        status = None
        rotate = 0
        for i in range(len(nums)-1):
            if rotate > 2:
                return False
            if nums[i] == nums[i+1]:
                return False
            if not status:
                if nums[i] > nums[i+1]:
                    return False
                status = "increasing"
                continue
            if status == "increasing":
                if nums[i] > nums[i+1]:
                    status = "decreasing"
                    rotate += 1
            elif status ==  "decreasing":
                if nums[i] < nums[i+1]:
                    status = "increasing"
                    rotate += 1
        return rotate == 2
