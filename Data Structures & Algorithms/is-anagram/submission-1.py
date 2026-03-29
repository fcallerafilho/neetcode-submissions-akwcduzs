class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 1
            else:
                sMap[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in tMap:
                tMap[t[i]] = 1
            else:
                tMap[t[i]] += 1

        if sMap == tMap:
            return True
        else:
            return False
        
