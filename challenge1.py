# 2+22+222+2222+...
def challenge(m, n):
    total = 0
    whole = 0
    i = 0
    while i<n:
        digit = m*(10**i)
        total += digit
        whole += total
        i = i+1
    
