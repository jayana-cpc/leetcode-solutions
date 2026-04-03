class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(word, curr):
            if not word:
                res.append(curr[:])
                return
            for i in range(1, len(word)+1):
                if isPalindrome(word[:i]):
                    curr.append(word[:i])
                    backtrack(word[i:], curr)
                    curr.pop()

        backtrack(s, [])
        return res
