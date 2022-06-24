from is_prime import is_prime # a function which checks if a value is prime and outputs a true or false value

# finds all primes from 2 to 'value' and returns a list unless 'value' is out of range (inclusive)
def primes_in_range(value):
    if not value > 1:
        return 0 # returns 0 (false) if 'value' is out of range
    list_of_primes = []
    for i in range(2,value+1): # checks values from 2 to value (inclusive)
        if is_prime(i):
            list_of_primes.append(i)
            continue
    return list_of_primes