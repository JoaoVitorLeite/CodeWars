# 8 kyu

def shortcut( s ):
    return s.translate(s.maketrans({'a':'', 'e':'', 'i':'', 'o':'', 'u':''}))