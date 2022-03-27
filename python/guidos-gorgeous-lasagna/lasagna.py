EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """
    Return remaining bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """
    Return total preperation time in minutes
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, cooking_time):
    """
    Return elapsed time in minutes
    """
    return preparation_time_in_minutes(layers) + cooking_time
