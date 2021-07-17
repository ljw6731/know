a = '여기는 \ n 와이즈만 \ n입니다.'
b = '여기는와이즈만입니다.'

# '' '
c = '여기는 \ t 와이즈만 \ t입니다. \ n 여기는 \ t 집 \ t입니다.'
print (유형 (a))
print (a)
print (b)
print (c)
점수 = 60
sen = '멋지네요.'
print ( '당신의 점수는 % d입니다. % s'% (score, sen))
print ( '당신의 점수는 {}입니다. {}'. format (score, sen))
print ( '당신의 점수는 {1}입니다. {0}'. format (score, sen))
print (f'당신의 점수는 {점수}입니다. {sen}')

string = '이것은 내 파이썬 프로젝트입니다 .'
print (len (문자열))
print (string.find ( 'p'))
print (string.count ( 'p'))
print (문자열)
print (string.strip ())
string_split = string.split ()
print (문자열 분할)

an = str ()
반면  하지 ( . ISNUMERIC () 과 렌 ( ) == 11 및 [ 0 : 3 ] == '010' )
    an = 입력 ( '전화 번호를 입력 해주세요. 숫자 만 입력 해주세요. 11 자리를 입력해야합니다.' )
an2 = an [ 0 : 3 ] + '-' + an [ 3 : 7 ] + '-' + an [ 7 : 11 ]
print ( f '당신이 입력 한 전화 번호는 { an2 } 입니다.' )