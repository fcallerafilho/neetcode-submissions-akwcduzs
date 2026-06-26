"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        maxTime = float('-inf')

        s_intervals = [[i.start, i.end] for i in intervals]
        s_intervals.sort()

        for meeting in s_intervals:
            if meeting[0] < maxTime:
                return False

            maxTime = max(maxTime, meeting[1])

        return True
