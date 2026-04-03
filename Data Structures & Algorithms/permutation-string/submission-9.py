class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Q: Keep track of s1 count?
        A: use Counter(s1) -> encodes it

        Q: How to check for a permutation?
        A: check if the encoding for the substring and s1 are equal.

        Q: How to encode each substring of s2. 
        A: Add and delete from the hashmap.

        Algorithm:
        1. Encode s1 -> Counter(s1)
        2. Encode s2 -> Counter(s2[:len(s1)])
        3. check if equal iniatilly
        3. l, r = 0, len(s1)
        4. for r in range(len(s2)):
        4a. remove s2[l] from hashmap
        4b. increment l+=1
        4c. add s2[r] to hashmap
        4d. if Counter(s1) == Counter(s2[:]): -> return True
        4e. if not, continue

        s1 = "abc", s2 = "lecabee"

        s1_map = Counter(s1) = {a: 1, b:1, c:1}
        s2_map = Counter(s2[:len(s1)]) = {c: 1, a: 1, b: 1}
        l = 1
        r = 4
        """
        if len(s1) > len(s2):
            return False
        s1_map = Counter(s1)
        s2_map = Counter(s2[:len(s1)])
        if s1_map == s2_map: return True
        l = 0
        for r in range(len(s1), len(s2)):
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            l += 1
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            if s1_map == s2_map: return True
        return False















