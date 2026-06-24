class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        window = []
        maxLen = 1
        
        while r < len(arr):
            if arr[r] == arr[r-1]:
                r += 1
                l = r - 1
                continue
            
            if arr[r] > arr[r-1]:
                window.append(True)
            if arr[r] < arr[r-1]:
                window.append(False)
            
            if len(window) >= 2 and window[-2] == window[-1]:
                window = [window[-1]]
                l = r - 1

            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen
            
            