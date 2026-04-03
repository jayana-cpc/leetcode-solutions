class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            count = tuple(count)
            if count in hm:
                hm[count].append(word)
            else:
                hm[count] = [word]
        return list(hm.values())

        