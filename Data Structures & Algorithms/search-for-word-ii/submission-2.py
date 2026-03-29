class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.index = -1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.res = []
        self.visited = {}

        def search(row, col, node):
            if min(row, col) < 0 or row >= len(board) or col >= len(board[0]):
                return
            if board[row][col] not in node.children:
                return
            if self.visited.get((row, col)):
                return
            
            node = node.children[board[row][col]]
            
            if node.word == True and node.index != -1:
                self.res.append(words[node.index])
                node.index = -1

            self.visited[(row, col)] = 1

            search(row+1, col, node)
            search(row-1, col, node)
            search(row, col+1, node)
            search(row, col-1, node)

            del self.visited[(row, col)]
            
        self.root = TrieNode()

        for i, word in enumerate(words):
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
            curr.index = i
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                search(row, col, self.root)

        return self.res
                    

            





        