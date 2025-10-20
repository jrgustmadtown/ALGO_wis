import sys

inputy = list(map(int, sys.stdin.buffer.read().split()))
k = inputy[0]
index = 1

def wis(sigma):
    n = len(sigma)
    sigma.sort(key=lambda x: x[1])    #jobs sorted by finish time
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

    return M[n] 

for _ in range(k):
    n = int(inputy[index])   
    index += 1
    jobs = [tuple(map(int, inputy[index+i*3 : index+i*3+3])) for i in range(n)]
    index+=(3*n)
    print(str(wis(jobs)))
    



