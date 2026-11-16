class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        limit = INT_MAX if sign == 1 else -INT_MIN
        res = 0
        x = abs(x)

        while abs(x) > 0:
            pop = (x%10)
            if res > limit // 10:
                return 0
            res = (res*10) + pop
            x = x//10
        return res * sign