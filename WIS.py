import sys

inputy = sys.stdin.read().splitlines()
k = int(inputy[0])
index = 1
outputy = []

def wis(jobs):
    n = len(jobs)
    sigma = sorted(jobs, key=lambda x: x[1])    #jobs sorted by finish time
    M = [0] * (n + 1)

    for j in range(1, n + 1): 
        sj, fj, vj = sigma[j - 1]  
       
        p = 0
        for i in range(j - 1):  # check previous jobs
            si, fi, vi = sigma[i]
            if fi <= sj:
                p = i + 1   

        M[j] = max(vj + M[p], M[j - 1]) #bellman

    return M[n]

for _ in range(k):
    jobs = []
    n = int(inputy[index])   
    index += 1
    for __ in range(n):
        s, f, v = inputy[index].split()
        jobs.append([int(s), int(f), int(v)])
        index += 1

    outputy.append(wis(jobs))

for _ in outputy:
    print(_)
    



