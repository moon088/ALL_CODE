#B

S = input()
count = ord("A")
for i in range(len(S)):
    moji = S[i]
    if count > ord(S[i]):
        print("No")
        exit()
    count = max(count, ord(moji))
print("Yes")

