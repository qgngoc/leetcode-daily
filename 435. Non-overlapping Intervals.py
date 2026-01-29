
def check_overlap(interval1, interval2):
    return interval1[1] > interval2[0]


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        graph = {}
        overlap = 0
        i = 0
        while i < len(intervals):
            # print(intervals, i)
            if len(intervals) <= 1:
                break
            if i == 0:
                i += 1
                continue
            if check_overlap(intervals[i-1], intervals[i]):
                overlap += 1
                if intervals[i-1][1] >= intervals[i][1]:
                    intervals.pop(i-1)
                else:
                    intervals.pop(i)
                i -= 1
                continue
            i += 1
        return overlap

