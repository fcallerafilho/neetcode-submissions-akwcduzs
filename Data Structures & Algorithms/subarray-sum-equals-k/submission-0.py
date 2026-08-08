class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        cnt = 0
        freqs = {}
        freqs[0] = 1

        for n in nums:
            total += n
            diff = total - k

            cnt += freqs.get(diff, 0)
            freqs[total] = 1 + freqs.get(total, 0)

        return cnt
