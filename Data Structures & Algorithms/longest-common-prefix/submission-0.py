class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        longest = max([len(s) for s in strs])

        for i in range(longest):
            isprefix = True
            for j in range(len(strs)):
                if i >= len(strs[j]):
                    isprefix = False
                    break
                elif strs[j][i] != strs[0][i]:
                    isprefix = False
                    break

            if isprefix:
                prefix += strs[0][i]
            else:
                break
                
        return prefix