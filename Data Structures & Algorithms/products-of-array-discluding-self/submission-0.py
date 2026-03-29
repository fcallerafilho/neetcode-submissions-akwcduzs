class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):
            prod = 1
            if i == 0:
                pre = []
            else:
                pre = nums[:i]

            post = nums[i+1:]
            subarray = pre + post

            for i in range(len(subarray)):
                prod *= subarray[i]

            products.append(prod) 

        return products       
