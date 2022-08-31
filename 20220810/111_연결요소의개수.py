# https://www.acmicpc.net/problem/11724
# 방향 없는 그래프가 주어졌을 때 연결요소 개수 구하기

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 인접 리스트 만들기
for _ in range(N):
    u, v = map(int, input().split())
    N[u].append(v)
    N[v].append(u)


def dfs(start):
    stack = [start]
    visited[start] = True
    cnt = 0

    while stack:
        cur = stack.pop()

        for i in N[cur]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                cnt += 1
    return print(cnt)

dfs(1)