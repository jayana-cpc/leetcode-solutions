class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        n = []
        sortedhashkeys = {}
        sortedhash = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        for key, value in sortedhash:
            sortedhashkeys[key] = value
        sortedhashkeyslist = list(sortedhashkeys)
        for key in range(k):
            res = sortedhashkeyslist[0]
            n.append(res)
            sortedhashkeyslist.remove(res)
        return n

        