n = int(input())
a = list(map(int, input().split()))

flg = False
cnt = 0
for i, v in enumerate(a, 1):
    if flg:
        flg = False
        continue

    if i == v:
        cnt += 1
        flg = True
print(cnt)
