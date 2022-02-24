def ones_complement(binary_number):
    aux = [i for i in range(0,len(binary_number)) if binary_number[i] == '0']
    bn = list(binary_number)
    for i in range(0,len(binary_number)):
        if i in aux:
            bn[i] = '1'
        else:
            bn[i] = '0'
    return ''.join(bn)

