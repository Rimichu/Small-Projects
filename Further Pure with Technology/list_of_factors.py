# Finds all the factors of an integer, returns a list
def list_of_factors(value):
    factor_list=[]
    for i in range(1,value+1):
        if value % i == 0:
            factor_list.append(i)
    return factor_list