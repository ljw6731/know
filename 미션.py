an=str()
while not (an.isnumeric() and (len(an) == 11)):
    an=input('전화번호를 입력해주세요.숫자만 입력해주세요.11자리를 입력해야 합니다.')
an2=an[0:2]+'-'+an[3:7]+'-'+an[7:11]
print(f'당신의 입력한 전화번호는 {an2}입니다.')