class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        sum_ = 0

        for L in range(len(arr)):
            sum_ = arr[L]
            if L + k <= len(arr):
                for R in range(L + 1, L + k):
                    sum_ += arr[R]
                
                if (sum_ / len(arr[L:L + k])) >= threshold:
                    cnt += 1

        return cnt

