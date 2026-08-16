class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        arr = []
        for num, freq in freqs.items():
            arr.append([freq, num])

        arr.sort()
        arr.reverse()

        res = []
        for i in range(k):
            res.append(arr[i][1])

        return res