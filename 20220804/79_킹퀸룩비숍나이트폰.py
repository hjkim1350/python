# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 숫자와 문자가 섞인 문자열을 입력받음
# 문자열 one은 숫자 1, two는 2...로 문자열을 숫자로 치환
# 입력받은 값이 숫자면 그대로 유지

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


"""
def solution(s):
    answer = s

    num_d = {
        'zero' : "0",
        'one' : "1",
        'two' : "2",
        'three' : "3",
        'four' : "4",
        'five' : "5",
        'six' : "6",
        'seven' : "7",
        'eight' : "8",
        'nine' : "9"
    }
    
    for k, v in num_d.items():
            answer = answer.replace(k, v)

    return int(answer)
"""