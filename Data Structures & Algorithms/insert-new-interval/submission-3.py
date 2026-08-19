class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            currInterval = intervals[i]
            if newInterval[1] < currInterval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > currInterval[1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], currInterval[0]), max(newInterval[1], currInterval[1])]

        res.append(newInterval)
        return res