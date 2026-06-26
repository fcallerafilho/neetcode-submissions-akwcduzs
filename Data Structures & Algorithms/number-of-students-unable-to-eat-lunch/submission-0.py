class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        unable = 0

        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.pop(0)
                unable = 0
            else:
                student = students.popleft()
                students.append(student)
                unable += 1
            
            if unable == len(students):
                return len(students)

        return 0
