class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_id = Counter(s1)
        l = 0
        for r in range(len(s1)-1, len(s2)):
            window = Counter(s2[l:r+1])
            if window == s_id:
                return True
            l += 1
        return False
           
               