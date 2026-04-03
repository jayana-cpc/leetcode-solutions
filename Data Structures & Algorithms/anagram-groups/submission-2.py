class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        result = []
        for i in range(len(strs)):
            ss = "".join(sorted(strs[i]))
            if ss in hm.keys():
                hm[ss].append(strs[i])
            else:
                hm[ss] = [strs[i]]
        for i in hm.keys():
            result.append(hm[i])
        return result