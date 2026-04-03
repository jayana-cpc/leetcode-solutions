class GraphNode:
    def __init__(self, val):
        self.value = val
        self.dependents = set()
        self.inDegree = 0
class Graph:
    def __init__(self):
        self.verticies = {}
    def add(self, node):
        if node not in self.verticies:
           self.verticies[node] = GraphNode(node)
        return self.verticies[node]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = Graph()

        for i in range(numCourses):
            graph.add(i)
        
        for src, dest in prerequisites:
            graph.add(src).inDegree += 1
            graph.add(dest).dependents.add(graph.add(src))

        q = []
        for node in graph.verticies:
            if graph.add(node).inDegree == 0:
                q.append(graph.add(node))
        res = []
        while q:
            node = q.pop(0)
            res.append(node.value)
            for dep in node.dependents:
                dep.inDegree -= 1
                if dep.inDegree == 0:
                    q.append(dep)
        if len(res) == numCourses:
            return res
        else:
            return []











        