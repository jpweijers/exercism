STUDENTS = ["Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"]

PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


class Garden:

    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram.split('\n')
        self.students = students
        self.students.sort()

    def plants(self, name):
        i = self.students.index(name) * 2
        plants = self.diagram[0][i:i+2] + self.diagram[1][i:i+2]
        return [PLANTS[p] for p in plants]
