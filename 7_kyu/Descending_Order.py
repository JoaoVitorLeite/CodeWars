def descending_order(num):
    return int(''.join(map(str, sorted([int(i) for i in str(num)], reverse=True))))