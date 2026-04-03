class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prenums = [1, 1, 2, 8]
        # postnums = [48, 24, 6, 1]

        prenums = []
        postnums = []

        sum = 1
        for i in range(len(nums)):
            prenums.append(sum)
            sum *= nums[i] 
        sum = 1
        for i in reversed(range(len(nums))):
            postnums.append(sum)
            print(nums[i])
            sum *= nums[i]
        postnums.reverse()
        
        for i in range(len(nums)):
            nums[i] = prenums[i] * postnums[i]
        return nums


