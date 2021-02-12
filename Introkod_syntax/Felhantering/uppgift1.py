import numpy as np # impor ska egentligen vara import

def distance(p1, p2) :
    return np.sqrt(p1+p2) # return är felstavad

print(distance(0.5, 0.5)) #det ska inte vara en indexiering då blir det en lista av p1 utan man ska endast ha ()