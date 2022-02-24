def freq_seq(s, sep):
    return sep.join([str(s.count(l)) for l in s])
