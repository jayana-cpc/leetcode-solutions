class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = sorted(s1)

        for i in range(len(s2) - (len(s1) - 1)):
            if s2[i] in s1:
                if sorted(s2[i:i+len(s1)]) == s1Count:
                    return True
        return False     