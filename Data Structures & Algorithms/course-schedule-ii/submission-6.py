class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        schedule = defaultdict(list) # course : preresuisite
        visited = set()
        checked = set()
        res = []
        if not prerequisites:
            l = []
            for num in range(numCourses):
                l.append(num)
            return l

        for course, prerequisite in prerequisites:
            schedule[course].append(prerequisite)

        def dfs(course):
            if course in visited:
                return False
            if course in checked:
                return True

            visited.add(course)

            for c in schedule[course]:
                if not dfs(c):
                    return False

            visited.remove(course)
            res.append(course)
            checked.add(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
