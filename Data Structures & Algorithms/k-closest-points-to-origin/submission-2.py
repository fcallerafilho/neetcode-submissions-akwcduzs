class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []
        heapq.heapify_max(distances)
        
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush_max(distances, [distance, point[0], point[1]]) # nº of times we push: len(points)

            # nº of times we pop: len(points) - k
            if len(distances) > k:
                heapq.heappop_max(distances)

        while distances:
            distance, x, y = heapq.heappop_max(distances)
            res.append([x, y])

        return res
        



