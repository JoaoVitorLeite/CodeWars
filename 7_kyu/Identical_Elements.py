def duplicate_elements(m, n):
    if len(m) == 0 or len(n) == 0:
        return False
    else:
        for i in m:
            if i in n:
                return True
        return False