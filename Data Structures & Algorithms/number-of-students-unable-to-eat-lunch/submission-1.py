class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = len(students)
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = 0
        while count < student_count:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                student_count -= 1
                count = 0
            else:
                mover = students.popleft()
                students.append(mover)
                count += 1
        return student_count
