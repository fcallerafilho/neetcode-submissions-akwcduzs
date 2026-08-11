class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        total = 0
        cnt = 0

        for n in nums:
            total += n

            # k = total - "any prefixes that can be removed to sum up to k"
            prefixToRemove = total - k

            cnt += prefixSums.get(prefixToRemove, 0)

            prefixSums[total] = prefixSums.get(total, 0) + 1

        return cnt
            