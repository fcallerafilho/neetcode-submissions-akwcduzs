class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []

        set_1 = set(nums1)
        set_2 = set(nums2)

        res.append(list(set_1.difference(set_2)))
        res.append(list(set_2.difference(set_1)))

        return res