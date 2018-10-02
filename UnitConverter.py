import numpy as np

def common2au(x,identifier):
    if(identifier=='fs'):
        return x/2.418884326505e-2
    elif(identifier=='angstrom'):
        return x/5.2917721092e-1
    elif(identifier=='eV'):
        return x/27.21138602
    elif(identifier=='K'):
        return x/315775.13
    elif(identifier=='Debye'):
        return x/2.541746
    else:
        return None


def au2common(x,identifier):
    if(identifier=='fs'):
        return x*2.418884326505e-2
    elif(identifier=='angstrom'):
        return x*5.2917721092e-1
    elif(identifier=='eV'):
        return x*27.21138602
    elif(identifier=='K'):
        return x*315775.13
    elif(identifier=='Debye'):
        return x*2.541746
    else:
        return None
