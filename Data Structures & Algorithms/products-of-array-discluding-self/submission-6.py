class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1, 1, 2, 8]
        # postfix = [48,24,6,1]
        prefix = [1]
        postfix = [1]
        for num in nums[:-1]:
            prefix.append(prefix[-1]*num)
        nums.reverse()
        for num in nums[:-1]:
            postfix.append(postfix[-1]*num)
        postfix.reverse()
        print(prefix, postfix)
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
        return res