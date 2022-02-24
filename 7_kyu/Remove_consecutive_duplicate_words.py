def remove_consecutive_duplicates(s):
    aux = ['']
    for i in s.split(' '):
        if i != aux[-1]:
            aux.append(i)
    aux.remove('')
    return ' '.join(aux)