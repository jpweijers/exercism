class School:
    def __init__(self):
        self.students = {}
        self.add_list = []

    def add_student(self, name, grade):
        if name not in self.students:
            self.add_list.append(True)
            self.students[name] = grade
        else:
            self.add_list.append(False)

    def roster(self):
        grades = list(set(g for g in self.students.values()))
        grades.sort()

        roster = []
        for g in grades:
            roster += self.grade(g)

        return roster

    def grade(self, grade_number):
        grade_students = [s for s, g in self.students.items()
                          if g == grade_number]
        grade_students.sort()
        return grade_students

    def added(self):
        return self.add_list
