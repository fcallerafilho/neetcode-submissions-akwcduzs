class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        aux = []
        freqs = {}
        for i in range(len(nums)):
            freqs[nums[i]] = freqs.get(nums[i], 0) + 1

        for key, val in freqs.items():
            if not aux and val == 1:
                aux.append(key)
            elif val == 1 and key > aux[-1]:
                aux.append(key)

        return aux[-1] if aux else -1

