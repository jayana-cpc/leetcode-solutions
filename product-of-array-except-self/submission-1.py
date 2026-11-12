class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        pre = [1]
        counter = 0
        post = [1]
        for i in range(0, len(nums) - 1):
            post.insert(0, 0)

        for i in range(1, len(nums)):
            pre.append(nums[i-1] * pre[i-1])
        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i+1] * post[i+1]
            counter+=1
        for i in range(len(nums)):
            answer.append(pre[i] * post[i])
        return answer