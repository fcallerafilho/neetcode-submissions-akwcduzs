class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs_s, freqs_t = {}, {}

        for c in t:
            freqs_t[c] = 1 + freqs_t.get(c, 0)

        seen, need = 0, len(freqs_t)
        l = 0
        res = ''
        reslen = 0

        for i in range(len(s)):
            freqs_s[s[i]] = 1 + freqs_s.get(s[i], 0)

            if s[i] in freqs_t and freqs_s[s[i]] == freqs_t[s[i]]:
                seen += 1
            
            while seen == need:
                if s[l] not in freqs_t:
                    freqs_s[s[l]] -= 1
                    l += 1
                elif s[l] in freqs_t:
                    if res == '':
                        res = s[l:i+1]
                    else:
                        res = s[l:i+1] if len(s[l:i]) < len(res) else res

                    freqs_s[s[l]] -= 1
                    if freqs_s[s[l]] < freqs_t[s[l]]:
                        seen -= 1
                    l += 1
                                    
        return res

                
            


        
        
        

        

            

                

                    




