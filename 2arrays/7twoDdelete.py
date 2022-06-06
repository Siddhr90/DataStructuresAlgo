import numpy as np

twoDarray = np.array([[11,12,13,14], [15,16,17,18], [19,20,21,22], [23,24,25,26]])

newarray = np.delete(twoDarray,0,axis=0)

print(newarray)
print(twoDarray)