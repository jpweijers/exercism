class School:
    def __init__(self):
        self.students = []
        self.add_list = []

    def add_student(self, name, grade):
        if not [n for g, n in self.students if n == name]:
            self.students = sorted(self.students + [(grade, name)])
            self.add_list.append(True)
        else:
            self.add_list.append(False)

    def roster(self):
        return [n for i, n in self.students]

    def grade(self, grade_number):
        return [n for g, n in self.students if g == grade_number]

    def added(self):
        return self.add_list
