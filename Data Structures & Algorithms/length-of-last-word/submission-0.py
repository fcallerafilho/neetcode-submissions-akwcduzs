class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s.split(' ')) - 1, -1, -1):
            if not s.split(' ')[i]:
                continue
            else:
                return len(s.split(' ')[i])