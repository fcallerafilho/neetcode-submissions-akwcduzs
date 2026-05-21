class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        currPos = 0
        keymap = {}
        time = 0

        for i in range(len(keyboard)):
            keymap[keyboard[i]] = i

        for c in word:
            diff = abs(currPos - keymap[c])
            time += diff
            currPos = keymap[c]

        return time
