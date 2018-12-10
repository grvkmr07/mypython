def sphere(r):
    volume=(4*22*(r**3))/21
    surfacearea= (4*22*(r**2))/7
    return volume,surfacearea
def cone(r,h):
    volume= (22*r*r*h)/3
    l=((r**2)+(h**2))**(1/2)
    surfacearea= (22*r*l)/7
