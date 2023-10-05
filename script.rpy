# 게임에서 사용할 캐릭터를 정의합니다.
init: 
    # 캐릭터
    define 주인공 = Character('주인공', color="#ACA9BB")

    define 하늘 = Character('박하늘', color="#77CFF2")
    define 미소 = Character('김미소', color="#F2A0B6")
    define 지현 = Character('이지현', color="#F28705")

    # 이미지
    image bg goingToSchool = "images/bg/going-to-school-morning.png"

    # 효과
    # define slide_left = MoveTransition(duration=1.0, enter_xpos=1.0, leave_xpos=-1.0)

# 여기에서부터 게임이 시작합니다.
label start:
    $ protagonist_name = renpy.input("당신의 이름은 무엇인가요?")

    # 입력받은 이름이 비어 있을 경우 기본 이름 지정
    if not protagonist_name:
        $ protagonist_name = "김찐따"

    scene bg goingToSchool 
    "하늘색 봄 하늘 아래, [protagonist_name]은 약간의 떨림과 함께 중학교의 큰 정문 앞에 서 있었다."
    
    "[protagonist_name]는 학교의 건물을 올려다보며, 이곳에서 시작될 새로운 삶에 대한 기대와 불안이 교차했다."

    "[protagonist_name]의 발걸음은 무거웠다. 그럼에도 불구하고 [protagonist_name]는 교복을 입은 다른 학생들 사이로 천천히 걸어갔다."
    
    "그 때, 어디선가 익숙한 목소리가 들려왔다."



    

    return
