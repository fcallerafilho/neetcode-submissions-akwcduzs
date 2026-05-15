class Solution:
    def validWordSquare(self, words: List[str]) -> bool:        
        for c in range(len(words)):
            vertical_word = ''
            for r in range(len(words[c])):
                if r >= len(words) or c >= len(words[r]):
                    return False
                vertical_word += words[r][c]

            if words[c] != vertical_word:
                return False

        return True