class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Build adjacency list graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
    
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
    
    # Kahn's algorithm - BFS topological sort
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        completed = 0
    
        while queue:
            curr = queue.pop(0)
            completed += 1
        
        # Process neighbors
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
    
        return completed == numCourses