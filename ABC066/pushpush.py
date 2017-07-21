n = int(input())
s = input().split()
s1 = s[::2]
s2 = s[1::2]

if s2:  # 2文字以上なら
    if len(s) % 2:  # 偶数なら
        print(" ".join(s1[::-1]) + " " + " ".join(s2))
    else:  # 奇数なら
        print(" ".join(s2[::-1]) + " " + " ".join(s1))
else:  # 1文字なら
    print(" ".join(s1))
