class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        while True:
            if len(str(n)) == 1 and n != 7 and n != 1:
                return False
            total = 0
            for i in str(n):
                total += int(i) ** 2
            n = total
            if total == 1:
                return True
            
            
                
                
        