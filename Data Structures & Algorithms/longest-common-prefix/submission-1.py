class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        
        for i in range(min([len(s) for s in strs])):
            isprefix = True
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    isprefix = False
                    break

            if isprefix:
                prefix += strs[0][i]
            else:
                break
                
        return prefix