class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countCharFreq = [0] * 26
        s1CharFreq = [0] * 26

        for c in s1:
            s1CharFreq[ord(c) - ord('a')] += 1

        print(s1CharFreq)           

        for i in range(len(s1), len(s2)+1):
            window = s2[i - len(s1):i]

            for c in window:
                countCharFreq[ord(c) - ord('a')] += 1  

            if countCharFreq == s1CharFreq:
                return True
            else:
                countCharFreq = [0] * 26
       
        return False

            