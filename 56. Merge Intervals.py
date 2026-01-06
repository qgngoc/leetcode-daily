from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        minn = intervals[0][0]
        maxx = intervals[0][1]
        merged = []
        for interval in intervals[1:]:
            if interval[0] > maxx:
                merged.append([minn, maxx])
                minn = interval[0]
                maxx = interval[1]
            else:
                maxx = max(interval[1], maxx)
        merged.append([minn, maxx])
        return merged
