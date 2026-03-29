class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []

        for i in range(len(nums)):
            res.append(nums[(i - k) % len(nums)])
            
        nums[:] = res[:]