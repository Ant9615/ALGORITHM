# s = 'bbbb'
s = input()
lst = list(s)
slen = len(s)
answer = [-1]*26

for k in range(slen):
    if answer[ord(lst[k])-97] == -1:
        answer[ord(lst[k])-97] = k

for ans in answer:
    print(ans, end=' ')
