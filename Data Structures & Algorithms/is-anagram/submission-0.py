class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        
        yup = {}
        puy = {}
        for i in range(len(s)):
            if(s[i:i+1] in yup.keys()):
                yup[s[i:i+1]] = yup.get(s[i:i+1]) + 1
            else:
                yup[s[i:i+1]] = 1
        for i in range(len(t)):
            if(t[i:i+1] in puy.keys()):
                puy[t[i:i+1]] = puy.get(t[i:i+1]) + 1
            else:
                puy[t[i:i+1]] = 1
        if(len(yup.keys()) != len(puy.keys())): return False

        for i in range(len(yup.keys())):
            if yup.get(s[i:i+1]) != puy.get(s[i:i+1]): return False
        
        return True
        