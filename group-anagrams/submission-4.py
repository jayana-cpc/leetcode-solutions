class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            res = ''.join(sorted(i))
            if res in hashmap.keys():
                hashmap[res].append(i)
            else:
                hashmap[res] = [i]
        result = []
        for i in hashmap.keys():
            result.append(hashmap.get(i))
        return result


        