class Graph:
    def __init__(self):
        self.verticies = {}
    def add(self, node):
        if node not in self.verticies:
            self.verticies[node] = GraphNode(node)
        return self.verticies[node]

class GraphNode:
    def __init__(self, val):
        self.value = val
        self.inDegree = 0
        self.dependents = set()
   
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = Graph()
        for i in range(numCourses):
            graph.add(i)
        for src, dest in prerequisites:
            node1 = graph.add(src)
            node2 = graph.add(dest)
            node1.inDegree += 1
            node2.dependents.add(node1)

        q = []
        for node in graph.verticies:
            if graph.verticies[node].inDegree == 0:
                q.append(graph.verticies[node])
        print(graph.verticies)
        finish = 0
        while q:
            node = q.pop(0)
            finish += 1
            for dep in node.dependents:
                dep.inDegree -= 1
                if dep.inDegree == 0:
                    q.append(dep)
        
        return finish == numCourses


            
        
        

