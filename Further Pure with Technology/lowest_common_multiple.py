# Finds the lowest common multiple between 2 positive integers, outputs an integer
def lowest_common_multiple(value1,value2):
    for i in range(1,value1+1):
        if i * value2 % value1 == 0:
            return i * value2