class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        total = 0
        l = 0

        for r in range(len(arr)):
            total += arr[r]
            while r - l + 1 > k and l < len(arr):
                total -= arr[l]
                l += 1
            if r - l + 1 == k and total/k >= threshold:
                count += 1
        return count