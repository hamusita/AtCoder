N, M = int(input().split())
 
f = []
s = []
for i in range(M):
    a = list(map(int, input().split()
    if a[0] == 1:
        f.append(s)
    elif a[1] == N:
        s.append(s)
a = 0
for i in f:
    for j in s:
        if i[1] == j[0]:
            print("POSSIBLE")
            a = 1
if a :
    print("IMPOSSIBLE")

