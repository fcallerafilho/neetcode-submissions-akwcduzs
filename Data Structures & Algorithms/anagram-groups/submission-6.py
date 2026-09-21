class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charsToAnagram = {}

        for s in strs:
            chars = [0]*26
            for c in s:
                chars[ord(c)-ord('a')] += 1
            chars_tuple = tuple(chars)
            charsToAnagram[chars_tuple] = charsToAnagram.get(chars_tuple, [])
            charsToAnagram[chars_tuple].append(s)
        
        return [anagram for anagram in charsToAnagram.values()]
