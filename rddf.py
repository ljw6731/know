 파이 게임 가져 오기
수입  OS
수입  시스템
 무작위로 가져 오기
수입  시간

# ----- [게임 창 초기 위치] -----

win_posx  =  700
win_posy  =  300
os . environ [ 'SDL_VIDEO_WINDOW_POS' ] =  "% d, % d"  % ( win_posx , win_posy )

# ----- [윈도우 창 설정] -----

WINDOW_WIDTH  =  540
WINDOW_HEIGHT  =  600
그리드  =  30
GRID_WIDTH  =  int ( WINDOW_WIDTH  /  GRID )
GRID_HEIGHT  =  int ( WINDOW_HEIGHT  /  GRID )

# ===== [색상 설정] =====

검정  =  0 , 0 , 0
흰색  =  255 , 255 , 255
빨간색  =  255 , 0 , 0
녹색 1  =  25 , 102 , 25
녹색 2  =  51 , 204 , 51
녹색 3  =  233 , 249 , 185
파란색  =  17 , 17 , 212
LIGHT_PINK1  =  255 , 230 , 255
LIGHT_PINK2  =  255 , 204 , 255

NORTH  = ( 0 , - 1 )
남쪽  = ( 0 , 1 )
WEST  = ( - 1 , 0 )
동쪽  = ( 1 , 0 )


# ----- [스네이크 클래스] -----

 스네이크 클래스 :

    def  __init__ ( self ) :
        self . 길이  =  1
        self . create_snake ()
        self . color1  =  GREEN2
        self . color2  =  GREEN3
        self . head_color  =  GREEN1

    def  create_snake ( self ) :
        self . 길이  =  3
        self . 위치  = [( int ( WINDOW_WIDTH  /  2 ), int ( WINDOW_HEIGHT  /  2 ))]
        self . 방향  =  임의 . 선택 ([ NORTH , SOUTH , WEST , EAST ])
        글로벌  게임 점수
        game_score  =  0

    def  move_snake ( self , surface ) :

        # print (len (self.positions))
        머리  =  자기 . get_head_position ()
        x , y  =  자기 . 방향
        다음  = (( head [ 0 ] + ( x  *  GRID )) %  WINDOW_WIDTH , ( head [ 1 ] + ( y  *  GRID )) %  WINDOW_HEIGHT )
        만약  다음  에  자기 . 위치 [ 2 :] :
            self . create_snake ()
            게임 오버 ( 표면 )
        그렇지 않으면 :
            self . 위치 . 삽입 ( 0 , 다음 )
            경우  렌 ( 자기 . 위치 ) >  자기 . 길이 :
                del  self . 위치 [ - 1 ]

    def  draw_snake ( self , surface ) :
        에 대한  인덱스 , POS  에서  열거 ( 자기 . 위치 ) :
            만약  인덱스  ==  0 :
                draw_object ( surface , self . head_color , pos )
            elif  지수  %  2  ==  0 :
                draw_object ( surface , self . color1 , pos )
            그렇지 않으면 :
                draw_object ( surface , self . color2 , pos )

    def  game_control ( self , arrowkey ) :
        경우 ( arrowkey [ 0 ] *  - 1 , arrowkey [ 1 ] *  - 1 ) ==  자기 . 방향 :
            반환
        그렇지 않으면 :
            self . 방향  =  화살표 키

    def  get_head_position ( self ) :
        return  self . 위치 [ 0 ]


# ----- [먹이 클래스] -----

클래스  음식 :
    def  __init__ ( self ) :
        self . 위치  = ( 0 , 0 )
        self . 색상  =  빨간색
        self . randomize_food ()

    def  randomize_food ( self ) :
        self . 위치  = ( 랜덤 . randint ( 0 , GRID_WIDTH  -  1 ) *  GRID ,
                         무작위 . randint ( 0 , GRID_HEIGHT  -  1 ) *  GRID )

    def  draw_food ( self , surface ) :
        draw_object ( surface , self . color , self . position )


# ----- [전역] -----

def  draw_background ( 표면 ) :
    background  =  pygame . 직사각형 (( 0 , 0 ), ( WINDOW_WIDTH , WINDOW_HEIGHT ))
    파이 게임 . 무승부 . rect ( surface , WHITE , background )
    draw_grid ( 표면 )


def  draw_grid ( 표면 ) :
    위한  행  의  범위 ( 0 , INT ( GRID_HEIGHT )) :
        위한  COL  의  범위 ( 0 , INT ( GRID_WIDTH )) :
            if ( 행  +  열 ) %  2  ==  0 :
                rect  =  파이 게임 . 사각형 (( col  *  GRID , row  *  GRID ), ( GRID , GRID ))
                파이 게임 . 무승부 . rect ( surface , LIGHT_PINK1 , rect )
            그렇지 않으면 :
                rect  =  파이 게임 . 사각형 (( col  *  GRID , row  *  GRID ), ( GRID , GRID ))
                파이 게임 . 무승부 . rect ( surface , LIGHT_PINK2 , rect )


def  draw_object ( surface , color , pos ) :
    rect  =  파이 게임 . 직사각형 (( pos [ 0 ], pos [ 1 ]), ( GRID , GRID ))
    파이 게임 . 무승부 . rect ( surface , color , rect )
    파이 게임 . 무승부 . rect ( surface , WHITE , rect , 1 )


def  position_check ( snake , food_group ) :
    위해  식품  에  food_group :
         뱀 이라면 . get_head_position () ==  음식 . 위치 :
            글로벌  게임 점수
            게임 점수  + =  1
            뱀 . 길이  + =  1
            음식 . randomize_food ()


def  show_info ( surface , snake , speed ) :
    font  =  pygame . 글꼴 . SysFont ( 'malgungothic' , 35 )
    이미지  =  글꼴 . render ( f '점수 : { game_score } 뱀 길이 : { snake . length } LV : { int ( speed  //  2 ) } ' , True , BLUE )
    pos  =  이미지 . get_rect ()
    pos . move_ip ( 20 , 20 )
    파이 게임 . 무승부 . rect ( image , BLACK , ( pos . x  -  20 , pos . y  -  20 , pos . width , pos . height ), 2 )
    표면 . blit ( 이미지 , 위치 )


def  gameover ( 표면 ) :
    font  =  pygame . 글꼴 . SysFont ( 'malgungothic' , 50 )
    이미지  =  글꼴 . 렌더링 ( 'GAME OVER' , True , BLACK )
    pos  =  이미지 . get_rect ()
    pos . move_ip ( 120 , 220 )
    표면 . blit ( 이미지 , 위치 )
    파이 게임 . 디스플레이 . 업데이트 ()
    시간 . 수면 ( 2 )


플레이어  =  뱀 ()
실행  =  True
game_score  =  0


# ----- [먹이 그룹] -----

def  draw_food_group ( food_group , surface ) :
    위해  식품  에  food_group :
        음식 . draw_food ( 표면 )


음식  =  음식 ()
food_group  = []

위한  I  의  범위 ( 3 ) :
    음식  =  음식 ()
    food_group . 추가 ( 음식 )

위해  식품  에  food_group :
    인쇄 ( 음식 . 위치 )

# ----- [게임 루프] -----

파이 게임 . 초기화 ()
파이 게임 . 디스플레이 . set_caption ( 'SNAKE GAME' )
screen  =  pygame . 디스플레이 . set_mode (( WINDOW_WIDTH , WINDOW_HEIGHT ))
시계  =  파이 게임 . 시간 . 시계 ()

 실행 하는 동안 :

     파이 게임의 이벤트  를  위해 . 이벤트 . 가져 오기 () :
        경우  이벤트 . 유형  ==  pygame . 종료 :
            실행  =  False
        경우  이벤트 . 유형  ==  pygame . 키 다운 :
            경우  이벤트 . 키  ==  파이 게임 . K_q :
                실행  =  False
            경우  이벤트 . 키  ==  파이 게임 . K_UP :
                플레이어 . game_control ( NORTH )
            경우  이벤트 . 키  ==  파이 게임 . K_DOWN :
                플레이어 . game_control ( SOUTH )
            경우  이벤트 . 키  ==  파이 게임 . K_RIGHT :
                플레이어 . game_control ( EAST )
            경우  이벤트 . 키  ==  파이 게임 . K_LEFT :
                플레이어 . game_control ( WEST )

    draw_background ( 화면 )
    플레이어 . move_snake ( 화면 )
    position_check ( player , food_group )
    플레이어 . draw_snake ( 화면 )
    draw_food_group ( food_group , screen )
    # food.draw_food (screen)
    속도  =  플레이어 . 길이  /  2
    show_info ( 화면 , 플레이어 , 속도 )
    파이 게임 . 디스플레이 . 뒤집기 ()
    파이 게임 . 디스플레이 . 업데이트 ()
    시계 . 틱 ( 5  +  속도 )

# ----- [파이 게임 종료] -----

print ( '파이 게임 종료 됨' )
파이 게임 . 종료 ()
sys . 이탈 ()