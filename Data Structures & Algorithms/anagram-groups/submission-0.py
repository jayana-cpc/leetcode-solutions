class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            if str(''.join(sorted(i))) in hashmap:
                hashmap[str(''.join(sorted(i)))].append(i)
            else:
                hashmap[str(''.join(sorted(i)))] = [i]

        result = []

        for i in hashmap.keys():
            result.append(hashmap.get(i))
        return result


        