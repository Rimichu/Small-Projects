# checks if a value is prime and outputs a 0 (false) or 1 (true)
def is_prime(value):
    if not (isinstance(value, int) and value > 1):
        return 0
    for i in range(2,(value//2) + 1):
        if value % i == 0:
            return 0
    return 1