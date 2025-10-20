import sys
from bisect import bisect_right

inputy = list(map(int, sys.stdin.buffer.read().split()))
k = inputy[0]
index = 1

def wis(sigma):
    n = len(sigma)
    sigma.sort(key=lambda x: x[1])    #jobs sorted by finish time
    
    f_ = [0]
    M = [0]

    for s, f, v in jobs:
        i = bisect_right(f_, s) - 1
        
        #compute halfs of the bellman sperately
        bell_l = v + M[i]
        bell_r = M[-1]
        f_.append(f)
        M.append(max(bell_l, bell_r)) # bellman

    return M[-1]

for _ in range(k):
    n = int(inputy[index])   
    index += 1
    jobs = [tuple(map(int, inputy[index+i*3 : index+i*3+3])) for i in range(n)]
    index+=(3*n)
    print(str(wis(jobs)))
    



