import numpy as np
def my_mult(m1,m2,N):
    m3=[0 for i in range(N*N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                m3[i*N+j]=m3[i*N+j]+m1[i*N+k]*m2[k*N+j]
    return m3

N=5
matr1=list(range(N*N))
matr2=list(range(N*N))

print(my_mult(matr1,matr2,N))