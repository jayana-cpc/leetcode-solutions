import heapq
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, preq in prerequisites:
            adj[preq].append(course)
            indegree[course] += 1
        
        heap = []

        for course, indegree_num in enumerate(indegree):
            if indegree_num == 0:
                heap.append(course)
        
        heapq.heapify(heap)
        res = []
        while heap:
            course = heapq.heappop(heap)
            res.append(course)
            
            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    heapq.heappush(heap, neighbor)

        return res if len(res) == numCourses else []   



        