test_case = int(input())

for i in range(1, test_case+1):
    result = 0
    score = 0
    OX = input()

    for j in range(0, len(OX)):
        if OX[j] == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)