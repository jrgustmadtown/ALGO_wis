import sys

inputy = sys.stdin.read().splitlines()
k = int(inputy[0])
index = 1
outputy = []

def wis(jobs):
    n = len(jobs)
    sigma = sorted(jobs, key=lambda x: x[1])    #jobs sorted by finish time
    M = [n]
    M[0] = 0

    for j in range(1, n):
        sj, fj, vj = sigma[j]
        rho = sorted(sigma[:j], key=lambda x: x[0]) #jobs before j sorted by start time

        #find largest finish time that is before sj
        max_fi = -float("inf")
        i=0
        for si, fi, vi in rho:
            if max_fi <= fi and fi <= sj:
                max_fi = fi
            i+=1
            
        #populate
        if max_fi == -float("inf"):
            M[i] = 0
        else:
            M[j] = max(M[j-1], M[i] + vj)

    return M[n]

for _ in range(k):
    jobs = []

    for __ in range(index):
        index+=1
        s, f, v = inputy[index].split()
        jobs.append([int(s), int(f), int(v)])
        index+=1

    outputy.append(wis(jobs))

for _ in outputy:
    print(_)
    



