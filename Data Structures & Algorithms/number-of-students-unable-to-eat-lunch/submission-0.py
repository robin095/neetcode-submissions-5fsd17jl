class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = len(students)
        count = 0
        while count < student_count:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                student_count -= 1
                count = 0
            else:
                mover = students.pop(0)
                students.append(mover)
                count += 1
        return student_count

        


        