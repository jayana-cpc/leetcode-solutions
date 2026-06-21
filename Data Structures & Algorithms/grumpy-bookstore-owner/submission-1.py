class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        biggest_diff = float("-inf")
        interval = 0
        curr_grumpy = 0
        curr_not = 0
        l = 0

        for r in range(len(customers)):
            if not grumpy[r]:
                curr_grumpy += customers[r]
            curr_not += customers[r]
            while r - l + 1 > minutes and l < len(customers):
                if not grumpy[l]:
                    curr_grumpy -= customers[l]
                curr_not -= customers[l]
                l += 1
            if r - l + 1 == minutes:
                diff = curr_not - curr_grumpy
                if diff > biggest_diff:
                    interval = (l, r)
                    biggest_diff = diff
        total = 0
        for i in range(interval[0]):
            if not grumpy[i]:
                total += customers[i]
        total += sum(customers[interval[0]:interval[1]+1])
        for i in range(interval[1]+1, len(customers)):
            if not grumpy[i]:
                total += customers[i]
        return total

