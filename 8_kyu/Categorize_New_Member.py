# 7 kyu

def open_or_senior(data):
    
    out = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            out.append("Senior")
        else:
            out.append("Open")
    return out

