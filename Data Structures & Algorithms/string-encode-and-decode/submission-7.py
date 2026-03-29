class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        if not strs:
            return s

        for i in range(len(strs)):
            s_len = len(strs[i])
            s += str(s_len)
            s += '#'
            s += strs[i]

        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j + 1 + length])
            i = j + 1 + length
        return res

