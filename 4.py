s = input()
count = 0
flag = 0
for i in range(len(s)):
    if s[i] != ' ' and flag == 0:
        count += 1
        flag = 1
    else:
        if s[i] == ' ':
            flag = 0
print(count)
