from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r, l = 0, 0 
        d = deque()
        res = []

        while r < len(nums):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)

            if l > d[0]:
                d.popleft()

            if (r - l) + 1 == k:
                res.append(nums[d[0]])
                l += 1

            r += 1

        return res

            


            

            

            
            


