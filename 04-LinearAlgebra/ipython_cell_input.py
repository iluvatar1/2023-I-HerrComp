from scipy import linalg
import numpy as np
import time # use time.process_time_ns() , compare with monotonic_ns()

# WARNINGS
# 1) Seed is not controlled. Expect different results per run

MINSIZE=1
MAXSIZE=7000
NSAMPLES=10
data = np.zeros((NSAMPLES, 3))
# YOUR CODE HERE
N = np.geomspace(MINSIZE, MAXSIZE, NSAMPLES, dtype=np.int64)
#print(N)

data = np.zeros((NSAMPLES, 2))

for ii in range(len(N)):
    A = np.random.rand(N[ii], N[ii])
    start = time.process_time_ns()
    #start = time.monotonic_ns()
    kappa = linalg.norm(A)*linalg.norm(linalg.inv(A))
    end = time.process_time_ns()
    #end = time.monotonic_ns()
    #print(f"{kappa=}")
    data[ii, 0] = N[ii]
    total_time = (end - start)*1.0e-9
    data[ii, 1] = total_time
    print(f"{N[ii]}\t {total_time}")
