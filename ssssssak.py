에서  ursina  수입  *
에서  ursina . mesh_importer  가져 오기  *
에서  ursina . 조립식 . health_bar  가져 오기  *
 무작위로 가져 오기

# 폰트 지정
텍스트 . default_font = 'fonts / malgun.ttf'
색상 . text_color = 색상 . 검정

# 전역 국가 지정
상자 = []
몬스터 = []
box_count  =  0
AREA_SIZE  =  30
BUTTON_SIZE  = ( .25 , .075 )
앱  =  Ursina ()
MAX_COUNT  =  30
monster_hits  =  0
grid_clear  =  참

# 사운드로드
background_music  =  오디오 ( 'sound / 07-Town.ogg' , pitch = 1 , loop = True , autoplay = True , loops = 10000 )
power_up  =  Audio ( 'sound / power_up_04.ogg' , pitch = 1 , loop = True , autoplay = False )
주의  =  오디오 ( 'sound / attention.wav' , pitch = 1 , loop = True , autoplay = False )

# 텍스쳐 모음
텍스처  = [ str ( x + 1 ) for  x  in  range ( 12 )]

# 전체 화면 지정
# window.fullscreen = True

# 몬스터 클래스
class  Monster ( Entity ) :
    def  __init__ ( self , ** kwargs ) :
        슈퍼 (). __init __ ()
        self . 충돌체  =  '상자'
        self . 속도  =  4
        self . last_time  =  시간 . 시간 ()
        self . turn_time  =  시간 . 시간 ()
        self . 본문  = []
        self . 조회수  =  0
        self . 위치 = Vec3 ( 10 , 10 , 10 )
        self . 회전 = Vec3 . 제로 ()
        self . 방향  =  Vec3 ( 0 , 0 , 0 )
        self . turn  =  True

        에 대한  키 , 값  에  kwargs로 . 항목 () :
            setattr ( self , key , value )

    def  업데이트 ( self ) :
         시간 이면 . 시간 () -  자기 . turn_time  >  3 :
            self . turn_time = 시간 . 시간 ()
            self . turn =  True

        경우  렌 ( 박스 ) > (100)  와  자기 . 회전 :
            box_temp = boxs [ random . randint ( 0 , 100 )]
            self . 방향  =  Vec3 ( box_temp . position - self . position ). 정규화 ()
            self . look_at ( box_temp , axis = 'left' )
            self . turn  =  False
        self . 위치  + =  self . 방향  *  자기 . 속도  *  시간 . dt  *  1

        self . move_body ()

    def  move_body ( self ) :
        "" "몸체 이동" ""
        경우  렌 ( 자기 . 몸 ) >  0 :
            self . 본문 [ 0 ]. 위치  =  자기 . 위치
            self . 본문 [ 0 ]. 회전  =  자기 . 회전
         시간 이면 . 시간 () -  자기 . last_time  >  0.2 :
            self . last_time  =  시간 . 시간 ()
            위한  I  의  범위 ( 렌 ( 자기 . 본체 ) -  1 , 0 , - 1 ) :
                self . 본문 [ i ]. 위치  =  자기 . 본문 [ i  -  1 ]. 위치
                self . 본문 [ i ]. 회전  =  자기 . 본문 [ i - 1 ]. 회전

# 주인공 클래스
클래스  Snake_camera ( 엔티티 ) :
    def  __init__ ( self , ** kwargs ) :
        슈퍼 (). __init __ ()
        self . 충돌체  =  '상자'
        self . 속도  =  5
        # self.origin_y = -.5
        self . camera_pivot  =  엔티티 ( parent = self , y = 2 )
        self . 조회수  =  0
        self . last_time  =  시간 . 시간 ()
        self . 본체  = [ 엔티티 ( 부모 = 장면 , 모델 = '커비' , 충돌체 = '구' , 질감 = 'kirby_body.png' , 위치 = ( - 15 , - 15 , - 15 ))]

        카메라 . parent  =  self . camera_pivot
        카메라 . 위치  = ( 0 , 0 , - 8 )
        카메라 . 회전  = ( 0 , 0 , 0 )
        카메라 . fov  =  90
        마우스 . 잠김  =  True
        self . mouse_sensitivity  =  Vec2 ( 40 , 40 )

        에 대한  키 , 값  에  kwargs로 . 항목 () :
            setattr ( self , key , value )

    def  업데이트 ( self ) :
        self . rotation_y  + =  마우스 . 속도 [ 0 ] *  self . mouse_sensitivity [ 1 ]

        self . camera_pivot . rotation_x-  =  마우스 . 속도 [ 1 ] *  self . mouse_sensitivity [ 0 ]
        self . camera_pivot . rotation_x  =  클램프 ( 자기 . camera_pivot . rotation_x , - 90 , 90 )

        self . 방향  =  Vec3 ( self . forward  * ( 1  -  held_keys [ 's' ]) +  self . right  * ( held_keys [ 'd' ] -  held_keys [ 'a' ]))
                              + 자기 . up  * self . camera_pivot . rotation_x / - 80 * ( 1  -  held_keys [ 'S' ])). 정규화 ()
        origin  =  self . world_position
        self . 위치  + =  self . 방향  *  자기 . 속도  *  시간 . dt * 0.5

        # 자기 몸과 충돌 확인
        경우  렌 ( 자기 . 몸 ) > 3 :
            대한  난  에  자기 . 본문 [ 6 :] :
                hit_info  =  self . 교차 ( i )
                 hit_info 인 경우 . 히트 :
                    신청 . 일시 중지 ()
                    out  =  Text ( text = '자기 몸 이랑 부딪혀서 죽음' , color = color . red , position = ( 0 , 0.4 ), origin = ( 0 , 0 ),
                               스케일 = 2 )
                    파괴 ( out , delay = 2 )
                    main_menu . 활성화 ()
                    마우스 . 잠김  =  거짓

        self . move_body ()

    정의  입력 ( self , key ) :
        만약  키  ==  'w' :
            self . 속도  + =  1
        만약  키  ==  'D' :
            self . 속도  -=  1



    def  move_body ( self ) :
        경우  렌 ( 자기 . 몸 ) > 0 :
            self . 본문 [ 0 ]. 위치  =  자기 . 위치
         시간 이면 . 시간 () - 자기 . last_time > 0.2 :
            self . last_time = 시간 . 시간 ()
            위한  I  의  범위 ( 렌 ( 자기 . 본체 ) - 1 , 0 , - 1 ) :
                self . 본문 [ i ]. 위치  =  자기 . 본문 [ i - 1 ]. 위치
        대한  난  에  자기 . 몸 :
            i . 회전  + =  VEC3 ( 0 , 랜덤 . randint ( 5 , 10 ), 0 )

# 피자 클래스
클래스  Voxel ( Entity ) :
    def  __init__ ( self , position  = ( 0 , 0 , 0 )) :
        슈퍼 (). __init __ (
            부모  =  장면 ,
            위치  =  위치 ,
            모델  =  임의 . 선택 ([ 'sphere' , 'cube' ]),
            텍스처  =  무작위 . 선택 ([ 'white_cube' , 'brick' ] + textures ),
            색상  =  색상 . 색상 ( 0 , 0 , 임의 . uniform ( 0.9 , 1 )),
            충돌체  =  '구'
        )
        self . lasttime  =  시간 . 시간 ()
        self . 조회수  =  0

    def  업데이트 ( self ) :
        글로벌  box_count
        글로벌  monster_hits
        # 회전
        self . rotation_y  + =  시간 . dt * 100

        # 색상 변경
        # time.time ()-self.lasttime> 1 :
        # self.lasttime = time.time ()
        # self.color = color.rgb (random.randint (0,255), random.randint (0,255), random.randint (0,255))

        hit_info  =  self . 교차 ( player1 )
         hit_info 인 경우 . 히트 :
            player1 . 조회수  + =  1
            ui . health_bar_1 . 값  =  player1 . 히트
            box_count-  =  1
            사운드  =  오디오 ( power_up . clip , volume = 0.1 )
            위한  I  의  범위 ( 4 ) :
                #follows = Entity (parent = scene, model = 'kirby', collider = 'sphere', texture = 'kirby_body.png', position = (-15, -15, -15))
                다음  =  엔티티 ( 부모 = 장면 , 모델 = '구' , 충돌체 = '구' , 위치 = ( - 15 , - 15 , - 15 ), 컬러 = 색 . RGB ( 255 , 91 , 173 ), 배율 = 0.7 )
                player1 . 몸 . 추가 ( 다음 )
            델  박스 [ 박스 . 색인 ( 자신 )]
            파괴 ( 자신 )

        대한  괴물  의  괴물 :
            hit_info  =  self . 교차 ( 몬스터 )
             hit_info 인 경우 . 히트 :
                괴물 . turn =  True
                monster_hits  + =  1
                box_count-  =  1
                위한  I  의  범위 ( 4 ) :
                    #follows = Entity (parent = scene, model = 'badboy', collider = 'box', texture = 'badboy.png'
                    #, position = (-15, -15, -15), rotation = monster.rotation)
                    follows  =  Entity ( parent = scene , model = 'sphere' , collider = 'sphere' , texture = 'brick' ,
                                     위치 = ( - 15 , - 15 , - 15 ), 컬러 = 컬러 . 검정 , 배율 = 0.8 )
                    괴물 . 몸 . 추가 ( 다음 )
                델  박스 [ 박스 . 색인 ( 자신 )]
                파괴 ( 자신 )

# 메뉴 클래스
class  MenuMenu ( Entity ) :
    def  __init__ ( self , ** kwargs ) :
        슈퍼 (). __init__ ( parent = camera . ui , ignore_paused = True )
        self . main_menu  =  엔티티 ( parent = self , enabled = True )
        self . options_menu  =  엔티티 ( parent = self , enabled = False )
        # self.background = Sprite ( 'shore', color = color.dark_gray, parent = self, x = 0, y = 0.4, z = -1)

        텍스트 ( "메뉴" , parent = self . main_menu , y = 0.4 , x = 0 , origin = ( 0 , 0 ), color = color . red )

        def  quit_game () :
            신청 . 종료 ()

        def  options_menu_btn () :
            self . options_menu . 활성화 ()
            self . main_menu . 비활성화 ()

        def  grid_btn () :
            글로벌  grid_clear
            grid_clear  =  하지  grid_clear

        def  다시 시작 () :
            글로벌  플레이어 1
            글로벌  몬스터

            에 대한  전  에서  재생기 . 몸 :
                파괴 ( i )
            파괴 ( player1 )
            대한  괴물  의  괴물 :
                에 대한  전  에서  몬스터 . 몸 :
                    파괴 ( i )
                del  monsters [ 몬스터 . 색인 ( 몬스터 )]
                파괴 ( 몬스터 )
            player1  =  Snake_camera ( texture = 'kirby_body.png' , 모델 = 'kirby' )
            신청 . 이력서 ()

        ButtonList ( button_dict = {
            "재시작" : Func ( restart ),
            "옵션" : Func ( options_menu_btn ),
            "경계보기" : Func ( grid_btn ),
            "게임 종료" : Func ( quit_game )
        }, y = 0 , parent = self . main_menu , ignore_paused = True )

        # [옵션 메뉴] 창 시작
        텍스트 ( "옵션 메뉴" , parent = self . options_menu , y = 0.4 , x = 0 , origin = ( 0 , 0 ))

        def  options_back_btn_action () :
            self . main_menu . 활성화 ()
            self . options_menu . 비활성화 ()

        버튼 ( "후면" , 부모 = 자기 . options_menu , Y = - 0.3 , 배율 = ( 0.1 , 0.05 ), 컬러 = RGB ( 50 , 50 , 50 ),
               on_click = options_back_btn_action )

        # [옵션 메뉴] 창 끝

        에 대한  키 , 값  에  kwargs로 . 항목 () :
            setattr ( self , key , value )

    정의  입력 ( self , key ) :
        만약  자기 . options_menu . 활성화 됨 :
            만약  키가  ==  "탈출" :
                self . main_menu . 활성화 ()
                self . options_menu . 비활성화 ()

        만약  키 == '공간' :
            신청 . 이력서 ()

    def  업데이트 ( self ) :
        통과하다

# 유저 인터페이스 클래스
클래스  UI ( Entity ) :
    def  __init__ ( self ) :
        슈퍼 (). __init__ ( parent = camera . ui , ignore_paused = True )
        self . 점수  =  0
        self . frame  =  Entity ( parent = self , ignore_pauded = True ,)

        frame1 = 엔티티 ( model = 'quad' , parent  =  self , color = color . color ( 0 , 0 , 0 , 1 ), scale = ( 2 , 0.01 ), position = ( 0 , 0.49 ))
        프레임 2 = 엔티티 ( 모델 = '쿼드' , 부모  =  자기 , 컬러 = 색 . 컬러 ( 0 , 0 , 0 , 1 ), 배율 = ( 2 , 0.01 ), 위치 = ( 0 , - 0.49 ))
        frame3 = 엔티티 ( model = 'quad' , parent  =  self , color = color . color ( 0 , 0 , 0 , 1 ), scale = ( 0.01 , 1 ), position = ( 0.88 , 0 ))
        frame4 = 엔티티 ( 모델 = '쿼드' , 부모  =  자기 , 컬러 = 색 . 컬러 ( 0 , 0 , 0 , 1 ), 배율 = ( 0.01 , 1 ), 위치 = ( - 0.88 , 0 ))
        self . health_bar_1_text = 텍스트 ( 텍스트 = F '피자 먹은 수 { 재생기를 . 히트 } ' , 위치 = ( - 0.85 , 0.47 ), 컬러 = 색 . 청색 )
        self . health_bar_1  =  HealthBar ( 부모  =  자기 , bar_color = 색상 . 석회 . 색조 ( - 0.25 ), 진원도 = 0.5 , MAX_VALUE = MAX_COUNT )
        self . health_bar_1 . 값 = 0
    def  업데이트 ( self ) :
        글로벌  monster_hits
        파괴 ( self . health_bar_1_text )
        self . health_bar_1_text = 텍스트 ( 텍스트 = F '피자 먹은 수 { 재생기를 . 히트 }             몬스터의 갯수 { 렌 ( 괴물 ) }        몬스터가 먹은 피자 수 { monster_hits } ' , 위치 = ( - 0.85 , 0.47 ), 색상 = 색상 . 블루 )
        통과하다

# 메뉴 생성
main_menu  =  메뉴 메뉴 ()
main_menu . 비활성화 ()



# 플레이어 생성
#load_model ( 'badboy.blend') # 모델 초기 생성
#obj_to_ursinamesh (name = 'badboy', save_to_file = True)
player1  =  Snake_camera ( texture = 'kirby_body.png' , 모델 = 'kirby' )

#UI 생성
ui  =  UI ()

# 몬스터 생성
위한  I  의  범위 ( 20 ) :
    괴물 . append ( Monster ( texture = 'badboy.png' , 모델 = 'badboy' ))

# 배경 생성
backgrounds = [ str ( x ) for  x  in  range ( 21 , 34 )]
하늘 = 하늘 ( 질감 = 무작위 . 선택 ( 배경 ))

# 배경 음악 재생
background_music_playing = 오디오 ( background_music . clip , volume = 2 , loop = True )
"" "그리드 생성" ""
그리드 = []
그리드 . append ( Entity ( 모델 = Grid ( AREA_SIZE , AREA_SIZE ), scale = AREA_SIZE , color = color . color ( 0 , 0 , 0.5 , 0 ), rotation_x = 90 , position = ( 0 , AREA_SIZE / 2 , 0 ))))
그리드 . APPEND ( 엔티티 ( 모델 = 그리드 ( AREA_SIZE , AREA_SIZE는 ) 스케일 =는 AREA_SIZE , 컬러 = 색 . 컬러 ( 0 , 0 , 0.5 , 0 ), rotation_x = 90 , 위치 = ( 0 , - AREA_SIZE / 2 , 0 )))
그리드 . append ( Entity ( 모델 = 그리드 ( AREA_SIZE , AREA_SIZE ), 배율 = AREA_SIZE , 색상 = 색상 . 색상 ( 0 , 0 , 0.5 , 0 ), rotation_z = 90 , 위치 = ( 0 , 0 , AREA_SIZE / 2 )))
그리드 . APPEND ( 엔티티 ( 모델 = 그리드 ( AREA_SIZE , AREA_SIZE는 ) 스케일 =는 AREA_SIZE , 컬러 = 색 . 컬러 ( 0 , 0 , 0.5 , 0 ), rotation_z = 90 , 위치 = ( 0 , 0 , - AREA_SIZE / 2 )))
그리드 . append ( Entity ( 모델 = 그리드 ( AREA_SIZE , AREA_SIZE ), 배율 = AREA_SIZE , 색상 = 색상 . 색상 ( 0 , 0 , 0.5 , 0 ), rotation_y = 90 , 위치 = ( AREA_SIZE / 2 , 0 , 0 ))))
그리드 . APPEND ( 엔티티 ( 모델 = 그리드 ( AREA_SIZE , AREA_SIZE는 ) 스케일 =는 AREA_SIZE , 컬러 = 색 . 컬러 ( 0 , 0 , 0.5 , 0 ), rotation_y = 90 , 위치 = ( - AREA_SIZE / 2 , 0 , 0 )))

# 라이트
빛 ( 유형 = '포인트 라이트' , 색상 = ( 1 , 0.4 , 0.4 , 2 ))
빛 ( 유형 = '방향성' , 색상 = ( 0.7 , 0.7 , 0.7 , 3 ), 방향 = ( 3 , 3 , 1 ))

# 게임 루프
def  업데이트 () :
    글로벌  box_count
    글로벌  grid_clear
    # 박스 리젠
    경우  box_count  < AREA_SIZE ** 3 / 27000 * 200 :
        box_count  + =  1
        상자  =  복셀 ( 위치  = ( 랜덤 . randint ( - AREA_SIZE / 2 , AREA_SIZE / 2 ), 랜덤 . randint ( - AREA_SIZE / 2 , AREA_SIZE / 2 ), 랜덤 . randint ( - AREA_SIZE / 2 , AREA_SIZE / 2 )))
        상자 . 추가 ( 상자 )

    # 몬스터 리젠
    경우  렌 ( 몬스터 ) < 20 :
        괴물 . append ( Monster ( texture = 'badboy.png' , 모델 = 'badboy' ))

    # 게임 아웃
    만약  ABS ( 재생기 . 위치 . X ) > AREA_SIZE / 2 - 2  또는  ABS ( 재생기 . 위치 . Y ) > AREA_SIZE / 2 - 2  또는   ABS ( 재생기 . 위치 . Z ) > AREA_SIZE / 2 - 2 :
        대한  그리드  의  그리드 :
            그리드 . 색상 = ( 0 , 0 , 0.5 , 1 )
        out = Text ( text = '경고 !! 경계를 벗어났습니다. !!' , color = color . red , position = ( 0 , 0.4 ), origin = ( 0 , 0 ), scale = 2 )
        파괴 ( out , delay = 2 )
        사운드 = 오디오 ( 주의 . 클립 )
    만약  ABS ( 재생기 . 위치 . X ) >  AREA_SIZE / 2 + 2  또는  ABS ( 재생기 . 위치 . Y ) >  AREA_SIZE / 2 + 2  또는  ABS ( 재생기 . 위치 . Z ) >  AREA_SIZE / 2 + 2 :
        신청 . 일시 중지 ()
        out = Text ( text = '경계를 벗어나서 죽음.' , color = color . red , position = ( 0 , 0.4 ), origin = ( 0 , 0 ), scale = 2 )
        파괴 ( out , delay = 2 )
        main_menu . 활성화 ()
        마우스 . 잠김  =  거짓

    # 그리드 지우기
    만약  ABS ( 재생기 . 위치 . X ) <  AREA_SIZE / 2 - 5  및  ABS ( 재생기 . 위치 . Y ) <  AREA_SIZE / 2 - 5  및  ABS ( 재생기 . 위치 . Z ) <  AREA_SIZE / 2 - 5  및  grid_clear을 :
        대한  그리드  의  그리드 :
            그리드 . 색상  = ( 0 , 0 , 0.5 , 0 )

    # 몬스터와 충돌 확인
    대한  _monster  의  괴물 :
        대한  괴물  의  _monster . 몸 :
            hit_info = player1 . 본문 [ 0 ]. 교차 ( 몬스터 )
             hit_info 인 경우 . 히트 :
                신청 . 일시 중지 ()
                out = Text ( text = '몬스터와 부딪혀서 죽음' , color = color . red , position = ( 0 , 0.4 ), origin = ( 0 , 0 ), scale = 2 )
                파괴 ( out , delay = 2 )
                main_menu . 활성화 ()
                마우스 . 잠김  =  거짓

    # 몬스터가 플레이어에 충돌 할 경우
    대한  괴물  의  괴물 :
         player1의 플레이어  를  위해 . 몸 :
            hit_info = 몬스터 . 교차 ( 플레이어 )
             hit_info 인 경우 . 히트 :
                에 대한  전  에서  몬스터 . 몸 :
                    파괴 ( i )
                del  monsters [ 몬스터 . 색인 ( 몬스터 )]
                파괴 ( 몬스터 )

    # 피튼 30 개 먹으면 게임 종료
    경우  재생기 . 조회수  >  MAX_COUNT - 1 :
        신청 . 일시 중지 ()
        out  =  Text ( text = '성공 !! 게임을 클리어 했어요!' , color = color . red , position = ( 0 , 0.2 ), origin = ( 0 , 0 ), scale = 5 )
        파괴 ( out , delay = 2 )
        main_menu . 활성화 ()
        마우스 . 잠김  =  거짓

    # 몬스터가 못 나가게 막음
    대한  괴물  의  괴물 :
         괴물 이라면 . x  >  AREA_SIZE / 2  또는  monster . X  <  - AREA_SIZE / 2 :
            괴물 . X  * =  - 1
         괴물 이라면 . y  >  AREA_SIZE / 2  또는  monster . Y  <  - AREA_SIZE / 2 :
            괴물 . Y  * =  - 1
         괴물 이라면 . z  >  AREA_SIZE / 2  또는  괴물 . Z  <  - AREA_SIZE / 2 :
            괴물 . Z  * =  - 1

    # 경계선 보이기
    만약  held_keys [ '공간' ]
        대한  그리드  의  그리드 :
            그리드 . 색상 = ( 0 , 0 , 0.5 , 1 )


정의  입력 ( 키 ) :
    # 메뉴 보이기
     마우스 가 아니라면  . 잠김 :
        마우스 . 잠김 = True
     main_menu 인 경우 . 활성화 됨 :
        main_menu . 비활성화 ()
    만약  키 == 'F1' :
        신청 . 일시 중지 ()
        main_menu . 활성화 ()
        마우스 . 잠김 = 거짓

app . 실행 ()