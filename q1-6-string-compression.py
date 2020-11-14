 # string compression

s = input()
l = []
for i in range(len(s)):
    count = 0
    for j in range(0, len(s)):
        if s[i] == s[j]:
            count += 1
    l.append(s[i]+str(count))
print(set(l))
print(len(set(l)))