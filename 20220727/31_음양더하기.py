# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# Q) 정수 배열 absolutes와 정수들의 부호를 차례로 담은 불리언 배열 signs가 주어짐.
# 이에 따른 실제 정수들의 합을 구하여 return 하도록 solution 함수 완성하기

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
#            answer += int(absolutes[i])
            answer += absolutes[i]
            print(type(absolutes[i]))
        else:
            answer -= absolutes[i]
#            answer -= int(absolutes[i])
    return answer

if __name__ == '__main__':
    print(solution([4, 7, 12], [True, False, True]))
    print(solution([1, 2, 3], [False, False, True]))