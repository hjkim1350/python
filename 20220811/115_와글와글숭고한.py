# https://www.acmicpc.net/problem/17388
# 3개 대학의 참여도 합 100 이상이면 "OK"
# 참여도 합 100 미만이면 가장 낮은 대학 이름 첫단어 출력

Soongsil, Korea, Hanyang = map(int, input().split())

# 변수명을 return 하면 조금 더 타이핑이 줄어들 것 같음.
# 중첩 if문이 아니라, else 조건에 min()의 변수명을 return 받아 print 한다면?
if Soongsil + Korea + Hanyang >= 100:
    print("OK")
else:
    if min(Soongsil, Korea, Hanyang) == Soongsil:
        print("Soongsil")
    elif min(Soongsil, Korea, Hanyang) == Korea:
        print("Korea")
    else:
        print("Hanyang")