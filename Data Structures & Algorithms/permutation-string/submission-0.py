class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for i in s1:
            s1Count[i] = 1 + s1Count.get(i, 0)

        for i in range(len(s2) - (len(s1) - 1)):
            windowCount = {}
            for j in range(len(s1)):
                windowCount[s2[i + j]] = 1 + windowCount.get(s2[i + j], 0)
            if s1Count == windowCount:
                return True
        return False

        