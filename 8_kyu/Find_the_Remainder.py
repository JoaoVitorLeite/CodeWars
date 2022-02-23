# 8 kyu

def remainder(a,b):
    n,m = max(a,b), min(a,b)
    try:
        return n%m
    except:
        return None
