from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: list[str]) -> str:
        
        adj = defaultdict(set)
        indegree = {}
        for word in words:
            for char in word:
                indegree[char] = 0
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word2) < len(word1) and word1.startswith(word2):
                return ""
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        
        q = deque()

        for char, indeg in indegree.items():
            if indeg == 0:
                q.append(char)
        res = ""
        while q:
            char = q.popleft()
            res += char
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return res if len(res) == len(indegree) else ""