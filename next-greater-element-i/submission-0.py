class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                value = stack.pop()
                greater[value] = num
            stack.append(num)
        
        return [greater.get(element, -1) for element in nums1]



        