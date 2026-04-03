class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        l = 0
        s1_id = {}
        for char in s1:
            s1_id[char] = 1 + s1_id.get(char, 0)
        r = 0    
        window = {}
        while r - l + 1 <= len(s1):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            r += 1
        
        if s1_id == window:
            return True
        for rr in range(r, len(s2)):
            window[s2[rr]] = 1 + window.get(s2[rr], 0)
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                window.pop(s2[l])
            l += 1
            print(s1_id, window)
            if s1_id == window:
                return True
            
            
        return False
