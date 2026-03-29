class Solution:
    def groupAnagrams(self, strs: List[str]):
        ans = defaultdict(list)
        
        for s in strs:
            countCharFreq = [0] * 26

            for c in s:
                countCharFreq[ord(c) - ord("a")] += 1

            ans[tuple(countCharFreq)].append(s)

        print(ans)
        return list(ans.values())








        