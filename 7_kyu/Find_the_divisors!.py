def divisors(integer):
    aux = [i for i in range(2, integer) if integer % i == 0]
    if len(aux) == 0:
        return "{} is prime".format(integer)
    else:
        return aux