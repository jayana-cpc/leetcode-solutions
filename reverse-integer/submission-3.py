class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        limit = 2**31
        res = 0
        x = abs(x)

        while x > 0:
            pop = x%10
            if res > limit // 10:
                return 0
            res = (res*10) + pop
            x = x//10
        return res * sign