class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currPrefixSum = 0
        prefixSums = {0:1}
        res = 0
        for i in range(len(nums)):
            currPrefixSum += nums[i]
            prevPrefixSum = currPrefixSum - k

            if prevPrefixSum in prefixSums:
                res += prefixSums[prevPrefixSum]

            prefixSums[currPrefixSum] = prefixSums.get(currPrefixSum, 0) + 1

        return res