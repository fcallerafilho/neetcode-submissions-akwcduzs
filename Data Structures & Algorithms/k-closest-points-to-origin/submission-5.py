class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []

        for x, y in points:
            distance = ((x)**2 + (y)**2)
            distances.append([distance, x, y])

        # build the heap log(n) time
        heapq.heapify(distances)

        # pop k times, given that popping is a log(n) operation, time complexity is k(log(n))
        while k > 0:
            distance, x, y = heapq.heappop(distances)
            res.append([x,y])
            k -= 1

        return res