class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        # row index
        i = 0
        # negative means down
        dr = -1

        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i == 0:
                d = -1
            elif i == numRows - 1:
                # positive means up 
                d = 1
            i += -d
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)

        