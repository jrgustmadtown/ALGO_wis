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

        #find fi < sj
        l=0
        h=j-2
        p=0 #previous
        while l<=h:
            m = (l+h)//2
            if sigma[m][1] <= sj:
                p=m+1
                l=m+1
            else:
                h=m-1

        M[j] = max(M[j-1], M[p] + vj) #bellman

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
    



