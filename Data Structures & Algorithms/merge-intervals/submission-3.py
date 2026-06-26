class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merge = []

        for i in range(len(intervals)):
            merge.append(intervals[i])

            if len(merge) >= 2 and merge[-1][0] <= merge[-2][1]:
                curr = merge.pop()
                prev = merge.pop()
                merge.append([min(curr[0], prev[0]), max(curr[1], prev[1])])


        return merge