class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        prefix = strs[0]

        for word in strs[1:]:
            temp = ""
            for letter in range(min(len(word), len(prefix))):
                if word[letter] == prefix[letter]:
                    temp += word[letter]
                else:
                    prefix = temp
                    break
        return prefix

        


        