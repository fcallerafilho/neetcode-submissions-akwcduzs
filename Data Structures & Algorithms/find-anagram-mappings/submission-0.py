class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # from nums 1 to nums 2
        # mapping[i] = j

        hashmap = {}
        res = []

        for i in range(len(nums2)):
            hashmap[nums2[i]] = i

        for num in nums1:
            res.append(hashmap[num])

        return res