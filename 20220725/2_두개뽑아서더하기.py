# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    sum = 0
    
    for i in range(0, len(numbers)):
        for j in range (i+1, len(numbers)):
            #sum = int(numbers[i]) + int(numbers[j])
            answer.append(int(numbers[i]) + int(numbers[j]))
    answer = sorted(list(set(answer)))
    #answer.sort()
    
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))