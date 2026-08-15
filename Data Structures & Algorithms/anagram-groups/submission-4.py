class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {} # char count list : list of strings with it
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1

            strs_map[tuple(chars)] = strs_map.get(tuple(chars), [])
            strs_map[tuple(chars)].append(s)

        return list(strs_map.values())

            


