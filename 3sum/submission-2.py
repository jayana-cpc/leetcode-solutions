class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        res = set()  # Set to store unique triplets

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  # No triplet possible if the first element > 0

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return list(res)