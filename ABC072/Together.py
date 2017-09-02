import collections

N = input()
l = list(map(int, input().split()))

m = list(map(lambda x: x + 1, l))
n = list(map(lambda x: x - 1, l))

ans = collections.Counter(l + m + n).most_common(1)

print(ans)
