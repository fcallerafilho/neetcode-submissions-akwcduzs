class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        schedule = defaultdict(list) # course : prerequisite

        for course, prerequisite in prerequisites:
            schedule[course].append(prerequisite)

        def dfs(course):
            if course in visited:
                return False
            if not schedule[course]:
                return True
            
            visited.add(course)
            for prereq in schedule[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True