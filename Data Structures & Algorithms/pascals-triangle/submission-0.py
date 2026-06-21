class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[-1]*x for x in range(1, numRows+1)]
        
        for i in range(numRows):
            dp[i][0] = 1
            dp[i][-1] = 1
        
        # dp[i][j] = dp[2][1] = dp[1][0] + dp[1][1]
        # dp[i][j] = dp[4][1] = dp[3][0] + dp[3][1]
        # dp[i][j] = dp[4][2] = dp[3][2] + dp[3][1]
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        for i in range(0, numRows):   
            for j in range(i+1):  
                if dp[i][j] == -1:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        return dp