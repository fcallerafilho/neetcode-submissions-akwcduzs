class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        previousSums = {0:1} # prefixSum : frequency
        total, cnt = 0, 0


        for i in range(len(nums)):
            total += nums[i]
            sumToRemove = total - k

            cnt += previousSums.get(sumToRemove, 0)
            previousSums[total] = previousSums.get(total, 0) + 1

        return cnt

