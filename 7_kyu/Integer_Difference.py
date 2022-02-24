def int_diff(lst, n):
    cnt = 0
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if abs(lst[i] - lst[j]) == n:
                cnt += 1
    return cnt