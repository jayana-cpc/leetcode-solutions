class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = []
        counter = {}
        for word in strs:
            x = sorted(word)
            sword = ''.join(x)
            if sword in hashmap:
                pass
            else:
                hashmap.append(sword)
        for word in strs:
            sword = sorted(word)
            sword = ''.join(sword)
            if sword not in counter:
                counter[sword] = [word]
            elif sword in counter:
                counter[sword].append(word)
        x = [counter.values()]
        return counter.values()

        
