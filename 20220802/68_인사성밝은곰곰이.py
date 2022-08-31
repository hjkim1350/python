# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 제일 위 카드는 버리고 그 다음 제일 위 카드는 맨 밑으로 보내기
# 이에 따라 카드 N장이 있을 때 버린 카드를 순서대로 출력 후 마지막에 남게되는 카드 출력

def solution(s):
    answer = ""
    strs = ""
    num_dic = {
        "one": 1, "two": 2, "three": 3,
        "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "zero": 0
    }

    for i in s:
        if i.isdigit():
            answer += str(i)
#            print("test1", answer, strs)
        else:
            if num_dic.get(strs) == None:
                strs += str(i)
#                print("test2", answer, strs)
            else:
                strs = ""
                strs += str(i)
#                print("test3", answer, strs)
        
            if num_dic.get(strs) != None:
                answer += str(num_dic[strs])
    
    return print(int(answer))

if __name__ == "__main__":
	solution("123")