class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        res = []

        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        arr = []
        for key, val in freqs.items():
            arr.append([val, key])

        arr.sort()
        arr.reverse()

        for i in range(k):
            res.append(arr[i][1])

        return res

        



