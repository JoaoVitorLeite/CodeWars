def is_isogram(string):
    return len(set([i for i in string.lower()])) == len(string)