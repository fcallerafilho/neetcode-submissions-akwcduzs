class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        # original: rotated
        numbers = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        original = str(n)
        rotated = ''
        
        for i in range(len(original)-1, -1, -1):
            if original[i] not in numbers:
                return False
            rotated += numbers[original[i]]

        return rotated != original

        
        