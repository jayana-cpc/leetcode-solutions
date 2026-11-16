class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        back = 0
        while back < x:
            back = (back * 10) + (x % 10)
            x //= 10
        return back == x or x == back//10