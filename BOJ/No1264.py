import sys

while 1 :
    cnt = 0
    str = sys.stdin.readline().strip()
    if str == '#' :
        break
    for c in str :
        if c in 'aeiouAEIOU' :
            cnt += 1
    print(cnt)