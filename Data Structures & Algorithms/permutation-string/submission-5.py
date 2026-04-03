class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2): return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in s1:
            count1[ord(i) - ord('a')] += 1
        for i in s2[0:len(s1)]:
            count2[ord(i) - ord('a')] += 1
        print(count2) 
        l = 0
        for r in range(len(s1), len(s2)):
            print(count1, count2) 
            if count1 == count2:
                return True
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            count2[ord(s2[r]) - ord('a')] += 1
            

        return count1 == count2

            


        