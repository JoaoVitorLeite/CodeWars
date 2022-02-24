def triple_x(s):
    if s.find('x') == -1:
        return False
    else:
        idx = s.index('x')
        return s[idx:idx+3] == 'xxx'