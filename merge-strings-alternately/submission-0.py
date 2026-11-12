class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        end = ""
        print(word2[-2:])
        if len(word1) > len(word2): 
            end = word1[-1*(len(word1)-len(word2)):]
        elif len(word2) > len(word1):
            end = word2[-1*(len(word2)-len(word1)):]
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]
        return res+end
        