import sys

inputy = sys.stdin.read().splitlines()
k = int(inputy[0])
index = 1
outputy = []

def wis(jobs):
    n = len(jobs)
    sigma = sorted(jobs, key=lambda x: x[1])    #jobs sorted by finish time
    M = [0] * (n + 1)

    ij = [0] * (n + 1)  # ij is the largest index such that fij < sj
    for j in range(1, n + 1):
        sj, _, _ = sigma[j - 1]
        # find fi < sj
        lo, hi = 0, j - 2
        while lo <= hi:
            mid = (lo + hi) // 2
            if sigma[mid][1] <= sj:
                ij[j] = mid + 1
                lo = mid + 1
            else:
                hi = mid - 1

    for j in range(1, n + 1):
        sj, fj, vj = sigma[j - 1]
        M[j] = max(vj + M[p[j]], M[j - 1]) #bellman

    return M[n] # M[n] = solution

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
    



