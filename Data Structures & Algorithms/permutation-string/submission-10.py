class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1HM = Counter(s1)
        s2HM = Counter(s2[:len(s1) - 1])

        l = 0
        for r in range(len(s1)-1, len(s2)):
            s2HM[s2[r]] = s2HM.get(s2[r], 0) + 1
            if s1HM == s2HM:
                return True
            s2HM[s2[l]] -= 1
            if s2HM[s2[l]] == 0:
                del s2HM[s2[l]]
            l += 1
        return False
