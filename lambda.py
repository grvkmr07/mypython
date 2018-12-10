def abc(h):
    return lambda x: x+h
n = abc(5)
m = abc(7)
type(n)
print(m(5))

            
