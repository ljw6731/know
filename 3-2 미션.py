# print()
#
# for i in range(9):
#     print(f'{i+1} 단 구구단 입니다')
#     for j in range(9):
#         print(f'{i+1} X {j+1} = {(i+1)*(j+1)}')
# a = input('하트갯수')
# for i in a:
#     for j in range(int(i)):
#         print('♥', end='')
#     print()

# a = 8
# for i in range(9992):
#     a += 1
#     if a == 9:
#         continue
#     print(a,'번')
# print('끝')


# while True:
#     print('hello')


b = 0
for i in range(103):
    b += 1
    if b == 100:
        break
    print(b, '번')
