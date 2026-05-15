class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = 0
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i] 
            if i == len(s):
                return 1
            if i >= len(s) or s[i] == '0':
                return 0
            
            self.res += dfs(i+1)
            if int(s[i:i+2]) <= 26:
                self.res += dfs(i+2)

            cache[i] = self.res
            return self.res

        return dfs(0)