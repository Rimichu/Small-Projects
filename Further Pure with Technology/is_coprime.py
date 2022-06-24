# import a function which finds the highest common factor between two integer values, outputs an integer
from highest_common_factor import highest_common_factor

# a function which checks if two integer values are coprime, returns true or false
def is_coprime(value1,value2):
    if highest_common_factor(value1,value2) == 1:
        return True
    return False