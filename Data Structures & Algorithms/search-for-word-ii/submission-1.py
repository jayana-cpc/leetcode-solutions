class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
        curr.word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        res, seen = set(), set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        def search_node(word, node, r, c):
            if r in range(ROWS) and c in range(COLS) and (r, c) not in seen and board[r][c] in node.children:
                seen.add((r, c))
                node = node.children[board[r][c]]
                word += board[r][c]
                if node.end:
                    res.add(word)
                directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

                for x, y in directions:
                    newR, newC = r+x, c+y
                    search_node(word, node, newR, newC)
                seen.remove((r, c))
                
        for r in range(ROWS):
            for c in range(COLS):
                search_node("", trie.root, r, c)
        return list(res)



        








        