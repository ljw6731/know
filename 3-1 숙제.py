
a=input('숫자를 입력하세요.')# a=0
# b=0
# for i in range(1000):
#     a += 1
#     if a % 3 == 0:
#         print(a, end='   ')
#         continue
#     if a % 5 == 0:
#         print(a, end='   ')

# for i in range(1000):
#     a += 1
#     if (a % 3 == 0) or (a % 5 == 0) :
#         print(a, end='   ')


if (int(a) > 100) and (int(a) < 1001):
       print('작은수')
elif (int(a) > 1000) and (int(a) < 10001) :
        print('큰수')
elif int(a) > 10000:
    print('아주 큰 수')

