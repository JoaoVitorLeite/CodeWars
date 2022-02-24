from collections import OrderedDict

def compress(sentence):
    if len(sentence) == 0:
        return ''
    sentences = OrderedDict.fromkeys(sentence.lower().split(' ')).keys()
    aux = dict(zip(sentences, range(0, len(sentences))))
    print([aux[word] for word in sentence.lower().split(' ')])
    return ''.join(str(aux[word]) for word in sentence.lower().split(' '))
