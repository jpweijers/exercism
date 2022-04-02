def is_triangle(sides):

    if 0 not in sides:
        sides.sort()
        return sum(sides[0:2]) >= sides[2]
    return False


def equilateral(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    if is_triangle(sides):
        sides.sort()
        return sides[0] == sides[1] or sides[1] == sides[2]
    return False


def scalene(sides):
    unique_sides = []
    if is_triangle(sides):
        for side in sides:
            if side not in unique_sides:
                unique_sides.append(side)
    return len(unique_sides) == 3
