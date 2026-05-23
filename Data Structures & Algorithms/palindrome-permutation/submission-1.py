class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freqs = {}
        flag = False

        for c in s:
            freqs[c] = freqs.get(c, 0) + 1

        for val in freqs.values():
            if val % 2 != 0 and flag:
                return False
            elif val % 2 != 0:
                flag = True

        return True