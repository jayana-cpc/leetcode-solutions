class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = nums[:-1]
        last = nums[1:]
        if len(last) <= 1:
            return last[0]
        dp = [0] * (len(last) + 1)
        dp[0] = last[0]
        dp[1] = max(last[0], last[1])
        for i in range(2, len(last)):
            dp[i] = max(last[i] + dp[i-2], dp[i-1])
        
        last_amount =  dp[len(last) - 1]

        if len(first) <= 1:
            return first[0]
        dp = [0] * (len(first) + 1)
        dp[0] = first[0]
        dp[1] = max(first[0], first[1])
        for i in range(2, len(first)):
            dp[i] = max(first[i] + dp[i-2], dp[i-1])
        
        first_amount =  dp[len(first) - 1]

        return max(last_amount, first_amount)