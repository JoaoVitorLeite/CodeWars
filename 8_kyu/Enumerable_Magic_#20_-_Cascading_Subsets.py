#8 kyu

def each_cons(lst, n):
    out = []
    for i in range(0, len(lst)):
        aux = lst[i:i+n]
        if len(aux) == n:
            out.append(aux)
    return out