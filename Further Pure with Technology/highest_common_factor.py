from prime_factors import prime_factors # a function which finds all prime factors of a number

# find the highest common factor between 2 positive integers and outputs that value
def highest_common_factor(num1, num2):
    prime_factors1 = prime_factors(num1)
    prime_factors2 = prime_factors(num2)
    highest_common_factor = 1
    for prime_factor in prime_factors1:
        if prime_factor in prime_factors2:
            prime_factors2.remove(prime_factor)
            highest_common_factor *= prime_factor
        if prime_factors2 == []:
            break
    return highest_common_factor