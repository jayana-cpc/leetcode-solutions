class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        end = ""
        if len(word1) > len(word2): 
            end = word1[-1*(len(word1)-len(word2)):]
        elif len(word2) > len(word1):
            end = word2[-1*(len(word2)-len(word1)):]
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        return ''.join(res) + end
        