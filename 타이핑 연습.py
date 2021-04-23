"" "아래 나오는 문장과 코드를 직접 타이핑으로 작성하세요." ""

'''이렇게 하는 것이...'''

# 한줄
문자  =  'P'
print ( letter )   # P
print ( len ( letter ))   # 1
인사  =  'Hello, World!'   #
print ( greeting )   # Hello, World!
print ( len ( 인사말 ))   # 13
문장  =  "30 일 동안 파이썬 챌린지를 즐기시 길 바랍니다"
print ( 문장 )

# 여러 줄 작성
multiline_string  =  '' '저는 선생님이고 가르치는 것을 즐깁니다.
사람들에게 권한을 부여하는 것만 큼 보람있는 것을 찾지 못했습니다.
그래서 30 일 동안 파이썬을 만들었습니다. '' '
인쇄 ( multiline_string )
# 여러 줄 또 다른 방법
multiline_string  =  "" "저는 선생님이고 가르치는 것을 즐깁니다.
사람들에게 권한을 부여하는 것만 큼 보람있는 것을 찾지 못했습니다.
그래서 30 일 동안 파이썬을 만들었습니다. "" "
인쇄 ( multiline_string )

# 앞으로 다루기
first_name  =  '아사 베네'
last_name  =  'Yetayeh'
공백  =  ''
full_name  =  first_name  +  space  +  last_name
print ( full_name )   # Asabeneh Yetayeh

# 유행의 길이 확인
print ( len ( first_name ))   # 8
print ( len ( last_name ))   # 7
print ( len ( 성명 ) >  len ( 성명 ))   # 참
print ( len (전체 _ 이름 ))   # 15


# 앞으로 다루기
언어  =  'Python'
first_letter  =  언어 [ 0 ]
print ( first_letter )   # P
second_letter  =  언어 [ 1 ]
print ( second_letter )   # y
LAST_INDEX  =  LEN ( 언어 ) -  1
last_letter  =  언어 [ last_index ]
print ( last_letter )   #n

# 강화의-정수 표현
언어  =  'Python'
last_letter  =  언어 [ - 1 ]
print ( last_letter )   #n
second_last  =  언어 [ - 2 ]
print ( second_last )   # o

# 슬라이싱 예제

언어  =  'Python'
first_three  =  언어 [ 0 : 3 ]
last_three  =  언어 [ 3 : 6 ]
print ( last_three )   # hon

# 슬라이싱 또 다른 예제
last_three  =  언어 [ - 3 :]
print ( last_three )   # hon
last_three  =  언어 [ 3 :]
print ( last_three )   # hon

# 슬라이싱을 두 칸씩 건너 뛰는 방법
언어  =  'Python'
pto  =  언어 [ 0 : 6 : 2 ]   #
print ( pto )   # pto

# 이스케이프 문자 사용
print ( '모든 사람이 파이썬 도전을 즐기기를 바랍니다. \ n 당신은?' )   # 줄 바꿈
print ( '일 \ t 주제 \ t 운동' )
print ( '1 일차 \ t 3 \ t 5' )
print ( '2 일차 \ t 3 \ t 5' )
print ( '3 일차 \ t 3 \ t 5' )
print ( '4 일차 \ t 3 \ t 5' )
print ( '이것은 백 슬래시 기호 ( \\ )' )   # 백 슬래시를 쓰려면
print ( '모든 프로그래밍 언어에서 \ " Hello, World! \" '로 시작합니다. )

## 메소드 메소드 연습
# capitalize () : 첫 글튼 대문자로 변경

도전  =  '파이썬의 30 일'
print ( challenge . capitalize ())   # '파이썬의 삼십일'

# count () : 어디에 몇개가 있는지 숫자를 리턴

도전  =  '파이썬의 30 일'
print ( challenge . count ( 'y' ))   # 3
print ( challenge . count ( 'y' , 7 , 14 ))   # 1
print ( challenge . count ( 'th' ))   # 2`

# endswith () : 마지막에 오는 문자를 확인

도전  =  '파이썬의 30 일'
print ( challenge . endswith ( 'on' ))   # 참
print ( challenge . endswith ( 'tion' ))   # False

# expandtabs () : 탭의 크기를 변경

도전  =  '서른 \ t의 일 \ t 의 \ t 파이썬'
print ( challenge . expandtabs ())   # '파이썬의 30 일'
print ( challenge . expandtabs ( 10 ))   # '파이썬의 30 일'

# find () : 글자가 어디있는 곳을 리턴

도전  =  '파이썬의 30 일'
print ( challenge . find ( 'y' ))   # 5
print ( challenge . find ( 'th' ))   # 0

# format () 행렬의 포 맺을 지정
first_name  =  '아사 베네'
last_name  =  'Yetayeh'
직업  =  '선생님'
국가  =  '핀란드'
문장  =  '나는 {} {}입니다. 나는 {}. 나는 {}에 살고 있습니다. ' . 형식 ( first_name , last_name , job , country )
print ( 문장 )   # 나는 Asabeneh Yetayeh입니다. 나는 선생님이다. 저는 핀란드에 살고 있습니다.

반경  =  10
파이  =  3.14
면적  =  파이   # 반경 ## 2
result  =  '{}가있는 원의 면적은 {}입니다' . 형식 ( str ( 반경 ), str ( 면적 ))
print ( result )   # 10이있는 원의 면적은 314.0입니다.

# isalnum () : 알파벳과 숫자 로지 확인

도전  =  'ThirtyDaysPython'
print ( challenge . isalnum ())   # 참

도전  =  '30DaysPython'
print ( challenge . isalnum ())   # 참

도전  =  '파이썬의 30 일'
print ( challenge . isalnum ())   # False

도전  =  '파이썬 2019의 30 일'
print ( challenge . isalnum ())   # False

# isalpha () : 알파벳으로 이루어 졌는지 확인

도전  =  '파이썬의 30 일'
print ( challenge . isalpha ())   # 참
숫자  =  '123'
print ( num . isalpha ())   # False

# isdigit () : 숫자로 이루어 졌는지 확인

도전  =  '서른'
print ( challenge . isdigit ())   # False
도전  =  '30'
print ( challenge . isdigit ())   # 참

# isdecimal () : 십진수인지 확인

숫자  =  '10'
print ( num . isdecimal ())   # 참
숫자  =  '10 .5 '
print ( num . isdecimal ())   # 거짓

# isidentifier () : 평가 변수 명인지 확인

도전  =  '30DaysOfPython'
print ( challenge . isidentifier ())   # 숫자로 시작하기 때문에 False
도전  =  'thirty_days_of_python'
print ( challenge . isidentifier ())   # 참

# islower () : 소문자로만 이루어 졌는지 확인

도전  =  '파이썬의 30 일'
print ( challenge . islower ())   # 참
도전  =  '파이썬 30 일'
print ( challenge . islower ())   # False

# isupper () : 대문자로만 이루어 졌는지 확인

도전  =  '파이썬의 30 일'
print ( challenge . isupper ())   # False
도전  =  '파이톤의 30 일'
print ( challenge . isupper ())   # 참

# isnumeric () : 숫자로만 이루어 졌는지 확인

숫자  =  '10'
print ( num . isnumeric ())   # True
print ( 'ten' . isnumeric ())   # False

# join () :리스트를 합쳐 줌

web_tech  = [ 'HTML' , 'CSS' , 'JavaScript' , 'React' ]
결과  =  '#,' . 가입 ( web_tech )
print ( result )   # 'HTML # CSS # JavaScript # React'

# strip () : 앞쪽이나의 빈칸을 제거해 준다.

도전  =  '파이썬의 30 일'
print ( challenge . strip ())   # 30 일의 파이썬

# replace () : 문자를 대체 해줌

도전  =  '파이썬의 30 일'
print ( challenge . replace ( 'python' , 'coding' ))   # '코딩 30 일'

# split () : 단어로 나누어서리스트를 만듬

도전  =  '파이썬의 30 일'
print ( challenge . split ())   # [ 'thirty', 'days', 'of', 'python']

# title () : 모든 단어의 첫 글자를 대문자로 바꿈

도전  =  '파이썬의 30 일'
print ( challenge . title ())   # 파이썬 30 일

# swapcase () : 대문자는 소문자로 소문자는 대문자로 바꿈

도전  =  '파이썬의 30 일'
print ( challenge . swapcase ())   # THIRTY DAYS OF PYTHON
도전  =  '파이썬의 30 일'
print ( challenge . swapcase ())   # tHIRTY dAYS oF pYTHON

# startswith () : 첫 문장이 비교 문자와 같은지 비교

도전  =  '파이썬의 30 일'
print ( challenge . startswith ( 'thirty' ))   # 참
도전  =  '파이썬 30 일'
print ( challenge . startswith ( 'thirty' ))   # False