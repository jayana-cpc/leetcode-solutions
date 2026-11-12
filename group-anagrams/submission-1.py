class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashM = {}
        new = []
        final = []
        for i in range(len(strs)):
            new.append(''.join(sorted(strs[i]))) 
        for i in range(len(strs)):
            if new[i] in hashM:
                hashM[new[i]].append(strs[i])
            else:
                hashM[new[i]] = [strs[i]]
        for i in hashM:
            final.append(hashM[i])
        return final

