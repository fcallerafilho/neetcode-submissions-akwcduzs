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
            if node.word == True and node.index != -1:
                self.res.append(words[node.index])
                node.index = -1

            if row + 1 < len(board) and (row+1, col) not in self.visited and node.children.get(board[row+1][col]):
                self.visited[(row+1, col)] = 1
                search(row+1, col, node.children[board[row+1][col]])
                del self.visited[(row+1, col)]
            if row - 1 >= 0 and (row-1, col) not in self.visited and node.children.get(board[row-1][col]):
                self.visited[(row-1, col)] = 1
                search(row-1, col, node.children[board[row-1][col]])
                del self.visited[(row-1, col)]
            if col + 1 < len(board[0]) and (row, col+1) not in self.visited and node.children.get(board[row][col+1]):
                self.visited[(row, col+1)] = 1
                search(row, col+1, node.children[board[row][col+1]])
                del self.visited[(row, col+1)]
            if col - 1 >= 0 and (row, col-1) not in self.visited and node.children.get(board[row][col-1]):
                self.visited[(row, col-1)] = 1
                search(row, col-1, node.children[board[row][col-1]])
                del self.visited[(row, col-1)]
            
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
                if board[row][col] in self.root.children:
                    self.visited[(row, col)] = 1
                    search(row, col, self.root.children[board[row][col]])
                    del self.visited[(row, col)]

        return self.res
                    

            





        