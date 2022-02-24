def reverse_words(text):
    ans = ""
    word = ""
    for i in text:
        if i == ' ':
            ans += word[::-1]
            ans += i 
            word = "" 
        else:
            word += i
    return ans + word[::-1]