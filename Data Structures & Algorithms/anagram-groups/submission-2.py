class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        for s in strs:
            copy = list(s)
            copy.sort()
            copy = "".join(copy)
            if copy not in strs_map:
                strs_map[copy] = []
            strs_map[copy].append(s)
        return list(strs_map.values())
            