char = input()
char = char[0:-1]
while(1):
    if char[:(len(char) // 2)] == char[len(char) // 2:]:
        break
    else:
        char = char[0:-1]
print(len(char))
