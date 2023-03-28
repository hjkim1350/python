N = int(input())

cnt = 99

if N < 100:
    print(N)
else:
    for i in range(100, N+1):
        str_N = str(i)
        if int(str_N[0]) - int(str_N[1]) == int(str_N[1]) - int(str_N[2]):
            cnt += 1
    print(cnt)
