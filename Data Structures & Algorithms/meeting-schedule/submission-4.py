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
        intervals.sort(key=lambda i: i.start)
        for meeting in intervals:
            if meeting.start < maxTime:
                return False

            maxTime = max(maxTime, meeting.end)

        return True
