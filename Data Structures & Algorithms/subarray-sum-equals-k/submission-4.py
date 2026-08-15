class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        total = 0
        res = 0

        for n in nums:
            total += n

            # currPrefixSum - prevPrefixSum = k
            # currPrefixSum - k = prevPrefixSum
            prevPrefixSum = total - k

            res += prefixSums.get(prevPrefixSum, 0)
            
            prefixSums[total] = prefixSums.get(total, 0) + 1

        return res