# Dictionary(사전)란?
dict1 = {'name': '한사람', 'age': 22, 'gender': True}
print(dict1, type(dict1))

# 키 반복
for key in dict1.keys():
    print(key, ':', dict1[key])

# 값 반복
for value in dict1.values():
    print(value)

# 추가
dict1['hobby'] = ['술', '춤', '잠']
dict1['weight'] = 78.65
print(dict1)


# 동시에 여러요소 추가
dict1.update({'weight':67.8,'height:': 189.7})
print(dict1)

# 수정
dict1['hobby'] = ['술', '춤', '잠','게임','등산']
print(dict1)

# 요소 삭제
del dict1['weight']
print(dict1)

# (key,value)쌍 얻기
print(dict1.items())
for data in dict1.items():
    # print(data, type(data))
    print(data[0], ':',data[1])