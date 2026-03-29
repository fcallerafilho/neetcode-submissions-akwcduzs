class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []
        
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            distances.append((distance, point))
        
        distances.sort()
        i = 0

        while i < k:
            res.append(distances[i][1])
            i += 1

        return res
