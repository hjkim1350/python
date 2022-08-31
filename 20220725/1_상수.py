# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

intA, intB = input().split()

sangsuA = int(intA[::-1])
sangsuB = int(intB[::-1])

print(sangsuA if sangsuA > sangsuB else sangsuB)

#if sangsuA > sangsuB:
#    print(sangsuA)
#else:
#    print(sangsuB)

print(A if A > B else B)