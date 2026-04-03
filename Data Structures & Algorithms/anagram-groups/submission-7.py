class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for i in strs:
            ords = [0]*26
            for letter in i:
                ords[ord(letter) - ord('a')] += 1
            print(ords)
            ords = tuple(ords)
            print(ords)
            if ords in hm:
                hm[ords].append(i)
            else:
                hm[ords] = [i]
        return list(hm.values())

        