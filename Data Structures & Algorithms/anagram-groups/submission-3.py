class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hm = {}

        for i in strs:
            if ''.join(sorted(i)) in hm.keys():
                hm[''.join(sorted(i))].append(i)
            else:
                hm[''.join(sorted(i))] = [i]
        
        return hm.values()