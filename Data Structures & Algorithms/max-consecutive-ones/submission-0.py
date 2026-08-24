class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0

        for n in nums:
            if n == 0:
                cnt = 0
            else:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            
        return max_cnt
