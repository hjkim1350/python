inputyear = int(input())

if inputyear % 4 == 0:
    if inputyear % 400 == 0:
        print(1)
    elif inputyear % 100 == 0:
        print(0)
    else:
        print(1)
else:
    print(0)