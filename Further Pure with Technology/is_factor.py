# Function which checks if an integer is a factor of another integer, returns a boolean value
def is_factor(factor,value):
    if value % factor == 0:
        return True
    return False