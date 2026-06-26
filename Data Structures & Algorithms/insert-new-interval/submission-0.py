class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []

        for i in range(len(intervals)):
            # newInterval ends before current interval starts
            if newInterval[1] < intervals[i][0]:
                out.append(newInterval)
                return out + intervals[i:]

            # newInterval starts before current interval ends
            elif newInterval[0] > intervals[i][1]:
                out.append(intervals[i])
            
            # they overlap and need to be merged
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        out.append(newInterval)
        return out