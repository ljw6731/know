an=str()
while not (an.isnumeric() and (len(an) == 11)):
    an=input('전화번호를 입력해주세요.숫자만 입력해주세요.11자리를 입력해야 합니다.(-또는 뛰어쓰기하지말기.)')
an2=an[0:3]+'-'+an[3:7]+'-'+an[7:11]
sss=[an2]
print(sss)
