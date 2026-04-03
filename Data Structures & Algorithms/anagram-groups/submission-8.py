class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            sword = "".join(sorted(word))
            if sword in hm:
                hm[sword].append(word)
            else:
                hm[sword] = [word]
        return list(hm.values())