def solution(n,d):
    if d <= 0:
        return []
    else:
        aux = [int(i) for i in str(n)]
        return aux if d >= len(aux) else aux[len(aux)-d:]