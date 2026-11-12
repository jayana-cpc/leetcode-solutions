class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]

        for word in strs:
            if len(word) < len(shortest):
                shortest = word
        pref = shortest

        count = 0
        while count < len(shortest):
            count += 1
            good = True
            for word in strs:
                print(pref)
                if word[:len(pref)] != pref:
                    good = False
            if good:
                print("YAY", pref)
                return pref
            else:
                pref = pref[:-1]
        return ""
