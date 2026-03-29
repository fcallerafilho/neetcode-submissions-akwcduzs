class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            mid = (l + r) // 2 if l <= r else -1

            # array_partition_leftorright
            A_left_rightmost = nums1[mid] if mid >= 0 else float('-inf')
            A_right_leftmost = nums1[mid + 1] if mid + 1 < len(nums1) else float('inf')
            B_left_rightmost = nums2[half - (mid + 1) - 1] if half - (mid + 1) - 1 >= 0 else float('-inf')
            B_right_leftmost = nums2[half - (mid + 1)] if half - (mid + 1) < len(nums2) else float('inf')

            if A_left_rightmost <= B_right_leftmost and B_left_rightmost <= A_right_leftmost:
                if total % 2 != 0:
                    return float(min(A_right_leftmost, B_right_leftmost))
                else:
                    return (max(A_left_rightmost, B_left_rightmost) + min(A_right_leftmost, B_right_leftmost)) / 2
            elif A_left_rightmost > B_right_leftmost:
                r = mid - 1
            else:
                l = mid + 1
