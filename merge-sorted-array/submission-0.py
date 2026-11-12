class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [1, 2p1]

        # nums2 = [1p2]
        if m == 0:
            nums1.clear()
            for num in nums2:
                nums1.append(num)
            return 
        if len(nums2) == 0:
            return 
        
        p1 = 0
        p2 = 0
        inserts = 0
        while p1 < m + inserts:
            if p2 >= len(nums2):
                return
            if nums2[p2] <= nums1[p1]:
                nums1.insert(p1, nums2[p2])
                inserts += 1
                nums1.pop()
                p2 += 1
            elif nums2[p2] > nums1[p1]:
                p1 += 1
        while p1 < len(nums1):
            print(p1, nums1, p2, nums2)
            nums1[p1] = nums2[p2]
            p2+=1
            p1+=1

        