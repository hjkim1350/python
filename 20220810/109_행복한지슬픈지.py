# https://www.acmicpc.net/problem/10769
# 이모티콘 없으면 none 출력
# 행복한 이모티콘과 슬픈 이모티콘 수 동일: unsure
# 행복한 이모티콘이 많으면 happy
# 슬픈 이모티콘이 많으면 sad

N = input()
happy = N.count(":-)")
sad = N.count(":-(")

if (happy == sad and happy != 0):
    print("unsure")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
else:
    print("none")