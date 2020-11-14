# is unique

def isunique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return print('not unique')
    return print('unique')

s = str(input('input string: '))
isunique(s)
