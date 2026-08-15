class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}

        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        for i in range(len(s2) - len(s1) + 1):
            s2_map = {}
            for j in range(i, i+len(s1)):
                s2_map[s2[j]] = s2_map.get(s2[j], 0) + 1
                if s2_map == s1_map:
                    return True

        return False