# https://www.acmicpc.net/problem/1302
# 가장 많이 팔린 책 제목 출력
# 단, 많이 팔린 책이 여러 개일 경우 사전 순 가장 앞서는 제목 출력

N = int(input())
book_dic = {}
book_dic_sort = {}

for i in range(N):
    book = input()

    if book not in book_dic:
        book_dic.setdefault(book, 1)
    else:
        book_dic[book] = book_dic.get(book) + 1

book_dic_sort = dict(sorted(book_dic.items()))
print(max(book_dic_sort, key=book_dic_sort.get))