class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_id = Counter(s1)
        window = Counter(s2[:len(s1)-1])
        l = 0
        for r in range(len(s1)-1, len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if window == s_id:
                return True
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            
        return False
           
               