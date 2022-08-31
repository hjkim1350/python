# https://www.acmicpc.net/problem/2606
# 1번 컴퓨터가 바이러스 걸렸을 때, 이를 통해 감염되는 컴퓨터 수 출력
# DFS 활용
# 첫번째줄에는 컴퓨터의 수 주어짐
# 둘째줄에는 네트워크상에서 직접 연결되어 있는 컴퓨터쌍의 수 주어짐
# 셋째줄~마지막: 네트워크 상에 직접 연결되어 있는 컴퓨터 번호 쌍 주어짐

N = int(input())
cou = int(input())
coms = [[] for _ in range(N+1)]
visited = [False] * (cou+1)

# 인접 리스트 만들기
for _ in range(cou):
    c1, c2 = map(int, input().split())
    coms[c1].append(c2)
    coms[c2].append(c1)


def dfs(start):
    stack = [start]
    visited[start] = True
    cnt = 0

    while stack:
        cur = stack.pop()

        for i in coms[cur]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                cnt += 1
    return print(cnt)

dfs(1)