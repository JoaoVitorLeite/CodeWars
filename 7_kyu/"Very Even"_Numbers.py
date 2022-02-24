def is_very_even_number(n):
    aux = sum([int(i) for i in str(n)])
    if len(str(aux)) > 1:
        return is_very_even_number(aux)
    else:
        return aux % 2 == 0