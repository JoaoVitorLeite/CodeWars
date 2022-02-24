from collections import Counter

def validate_word(word):
    cnt = Counter(word.lower())
    mc = cnt.most_common()
    return mc[0][1] == mc[-1][1]