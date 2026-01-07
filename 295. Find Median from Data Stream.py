
def binary_search(arr, num):
    if num < arr[0]:
        return 0
    left = 0
    right = len(arr) - 1
    mid = int((left+right)/2)
    while left <= right:
        mid = int((left+right)/2)
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    if left == 0:
        return 0
    if left == len(arr):
        return len(arr) - 1
    return left
    # if abs(arr[left] - num) < abs(arr[left - 1] - num):
    #     return left
    # else:
    #     return left - 1

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        if num >= self.nums[-1]:
            self.nums.append(num)
            return
        index = binary_search(self.nums.copy(), num)
        self.nums.insert(index, num)
        return

    def findMedian(self) -> float:
        # print(self.nums)
        if len(self.nums) % 2 == 0:
            return (self.nums[int((len(self.nums)-1)/2)]+self.nums[int((len(self.nums)-1)/2)+1])/2.0
        else:
            return self.nums[int((len(self.nums)-1)/2)]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()