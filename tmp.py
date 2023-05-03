import numpy as np
import matplotlib.pyplot as plt

def print_two(X, Y):
    T = (X[1] + X[2]) / 2
    R = np.array([
        [ 1, X[0],X[0]**2, 0, 0, 0],
        [1, X[1], X[1]**2, 0, 0, 0],
        [0, 0, 0, 1, X[2], X[2]**2],
        [0, 0, 0, 1, X[3], X[3]**2],
        [1, T, T**2, -1, -T, -T**2],
        [0, 1, 2*T, 0, -1, -2*T],
        ])

    Z = np.hstack([Y,[0,0]])

    A = np.linalg.solve(R, Z)

    linsp  = np.linspace(X.min(), T)  
    f = np.poly1d(np.flip(A[0:3]))
    fun = [f(x) for x in linsp]
    plt.plot(linsp,fun)

    linsp  = np.linspace(T, X.max())  
    f = np.poly1d(np.flip(A[3:]))
    fun = [f(x) for x in linsp]
    plt.plot(linsp,fun)

for i in range(0, n - 4):
    print_two(X[i:i+4], Y[i:i+4])