class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
        
    def search(self, word: str) -> bool:
        def search_node(word, node):
            for i, char in enumerate(word):
                if char not in node.children:
                    if char == ".":
                        for x in node.children:
                            if search_node(word[i+1:], node.children[x]):
                                return True
                    return False
                else:
                    node = node.children[char]
            return node.end 
        return search_node(word, self.root)
        
