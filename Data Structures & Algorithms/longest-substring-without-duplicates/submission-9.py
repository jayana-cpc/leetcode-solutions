class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "zxyzxyz" -> 3
        "zzzz" -> 1
        "" -> 0
        Find the longest consecutive sequence of unique chars.
        Goal: O(n)

        Algorithm:
        Q: How to track unique char?
        A: Set() b/c constant look up time

        1. Define a seen = set() 
        2. For loop iterate through each char:
        2a. while char in seen -> move left pointer up.
        2aa. when we move pointer up, remove it from seen
        2b. add char to seen if its not in seen -> next loop
        2c. len(seen) is our answer (length of longest substring)
        2d. each loop, reset our longest length value
        2da. longest = max(longest, len(seen))
        
        seen = set(x, y, z)
        l: 1
        r: 4
        """
        seen = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while seen and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, len(seen))
        return longest


