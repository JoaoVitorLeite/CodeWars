def even_and_odd(n): 
    aux = [int(x) for x in str(n)]
    NE = list(filter(lambda _: _ % 2 == 0, aux))
    NO = list(filter(lambda _: _ % 2 != 0, aux))
    return (0 if len(NE) == 0 else int(''.join(str(e) for e in NE)), 0 if len(NO) == 0 else int(''.join(str(e) for e in NO)))