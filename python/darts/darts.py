def _coordinates_in_circle(x, y, radius):
    return x**2 + y**2 <= radius**2


def score(x, y):
    if _coordinates_in_circle(x, y, 1):
        return 10
    elif _coordinates_in_circle(x, y, 5):
        return 5
    elif _coordinates_in_circle(x, y, 10):
        return 1
    else:
        return 0
