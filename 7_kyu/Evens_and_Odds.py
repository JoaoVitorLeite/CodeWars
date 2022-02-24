def evens_and_odds(n):
    if n % 2 == 0:
        return bin(n).replace("0b", "")
    else: 
        return hex(n).lower().replace('0x', '')