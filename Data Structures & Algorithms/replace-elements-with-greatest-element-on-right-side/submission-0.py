class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = arr[-1]

        for i in range(len(arr)-2, -1, -1):
            currMax = max(arr[i], rightMax)
            arr[i] = rightMax
            if currMax > rightMax:
                rightMax = currMax
            
        arr[-1] = -1
            
        return arr