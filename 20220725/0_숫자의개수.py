# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

intA = int(input())
intB = int(input())
intC = int(input())

mul_total = intA*intB*intC
mul_total = str(mul_total)

#for i in range(0, 10):
#    i = str(i)
#    print(mul_total.count(i))

for i in range(10):
    print(mul_total.count(str(i)))