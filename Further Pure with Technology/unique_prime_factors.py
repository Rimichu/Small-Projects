from primes_in_range import primes_in_range # a function which finds all prime values in a range (inclusive)

#finds all unique prime factors of 'value' and outputs a sorted list unless 'value' is out of range
def unique_prime_factors(value):
    if not value > 1:
        return 0 # returns 0 (false) if 'value out of range
    list_of_primes = primes_in_range(value)
    list_of_prime_factors = []
    for i in list_of_primes:
        if value % i == 0:
            list_of_prime_factors.append(i)
            continue
    list_of_prime_factors.sort()
    return list_of_prime_factors