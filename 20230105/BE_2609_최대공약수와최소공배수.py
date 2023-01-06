# https://www.acmicpc.net/problem/2609
# 두 개의 자연수 입력받아 최대공약수 최소공배수 구하기

import math

N, M = map(int, input().split())

print(math.gcd(N, M))
print(math.lcm(N, M))