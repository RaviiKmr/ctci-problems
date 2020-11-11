# Check if one string is permutation of other
# Assuming both strings are of same length

a = input('first no: ')
b = input('second no: ')

a = "".join(sorted(a))
b = "".join(sorted(b))

for i in range(len(a)):
    if a[i] != b[i]:
        print('Not permutation')
        break
    else:
        print('Permutation')
        break
