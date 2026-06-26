"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals_sorted = [[i.start, i.end] for i in intervals]
        intervals_sorted.sort()
        
        minEndTimes = [intervals_sorted[0][1]]
        heapq.heapify(minEndTimes)

        for i in range(1, len(intervals_sorted)):
            if minEndTimes and intervals_sorted[i][0] >= minEndTimes[0]:
                heapq.heappop(minEndTimes)
            heapq.heappush(minEndTimes, intervals_sorted[i][1])

        return len(minEndTimes)