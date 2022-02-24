def valid_spacing(s):
    if s == '':
        return True
    elif len(s.strip()) != len(s):
        return False
    else:
        return not any([len(w.strip()) != len(w) or w == '' for w in s.split(' ')])