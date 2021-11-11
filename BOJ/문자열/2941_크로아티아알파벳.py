s = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
tmp = ''
count = 0
i = 0

while i < len(s):
    tmp += s[i]
    if len(tmp) == 1: i += 1
    else:
        count += 1
        if tmp in alphabet: tmp = ''
        else:
            if tmp == 'dz':
                if i == len(s)-1: count += 1; tmp = ''; break
                else:
                    if s[i+1] == '=': i += 1; tmp = ''
                    else: tmp = tmp[1]
            else: tmp = tmp[1]
        i += 1

if len(tmp) != 0: print(count + len(tmp))
else: print(count)