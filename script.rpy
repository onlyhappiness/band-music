# 게임에서 사용할 캐릭터를 정의합니다.
init: 
    # 캐릭터
    image Miso = "images/character/Miso/Default.png"
    
    define 주인공 = Character("[protagonist_name]", color="#ACA9BB")

    define 하늘 = Character('박하늘', color="#77CFF2")
    define 미소 = Character('김미소', color="#F2A0B6")
    define 지현 = Character('이지현', color="#F28705")

    # 이미지
    image bg goingToSchool = "images/bg/going-to-school-morning.png"
    image bg playground = "images/bg/playground.png"
    image bg library = "images/bg/library.png"

    # 효과
    transform scan_background:
        subpixel True # 부드러운 움직임을 위한 설정
        zoom 1.5 # 이미지를 1.5배로 확대합니다.
        xalign 0.5 # 이미지의 중앙을 기준으로 정렬합니다.
        linear 3 xalign 0.7 # 5초 동안 이미지를 오른쪽으로 움직입니다.
        linear 3 xalign 0.5 # 5초 동안 이미지를 원래 위치로 돌아옵니다.
        linear 3 zoom 1.0 # 원래 크기로 5초 동안 줌아웃됩니다.

# 여기에서부터 게임이 시작합니다.
label start:
    scene bg goingToSchool with fade

    "하늘색 봄 하늘 아래, 어린 시절의 추억과는 달리, 지금의 학교는 크고 복잡해 보였다."

    ####################################
    call get_player_name

    menu:
        "당신의 이름이 [protagonist_name]이(가) 맞나요?"
        "네, 맞아요.":
            "[protagonist_name](으)로 게임을 계속 진행합니다."
        "아니요, 다시 입력할게요.":
            jump get_player_name
    ####################################

    "[protagonist_name]은 약간의 떨림과 함께 고등학교의 큰 정문 앞에 서 있었다."
   
    "[protagonist_name]은 학교의 건물을 올려다보았다."

    scene bg goingToSchool at scan_background

    "이곳에서 시작될 새로운 삶에 대한 기대와 불안이 교차했다."

    "[protagonist_name]의 발걸음은 무거웠다."
    
    "그럼에도 불구하고 [protagonist_name]은 교복을 입은 다른 학생들 사이로 천천히 걸어갔다."
    
    "그 때, 어디선가 익숙한 목소리가 들려왔다."

    # "딴 생각에 잠기다 보니, 갑자기 뒤에서 누군가의 손이 그의 어깨를 툭 치는 소리가 들려왔다."

    미소 "야! [protagonist_name]!"

    scene bg goingToSchool with hpunch

    "[protagonist_name]은 목소리의 주인을 찾아본다."

    미소 "누구게~? 완전 딴 사람이 됐네?!"

    "[protagonist_name]은 놀라서 뒤를 돌아보니, 밝은 웃음으로 미소가 서 있었다."

    show Miso with dissolve

    미소 "너 여기 학교로 전학왔어?!"

    "김미소, 어린 시절 친하게 지낸 친구다."
    "미소는 그 이름만큼이나 상쾌하고 밝은 에너지를 가진 친구이다."
    "어린 시절에는 늘 호기심과 즐거움으로 많았고, 밝게 웃는 그녀의 모습은 주변 사람들에게 기쁨을 전하는 친구였다."

    "고등학생이 된 미소의 길게 흘러내리는 분홍 머리는 그녀의 활발한 성격을 더욱 돋보이게 하는 것 같다."

    주인공 "어.. 오랜만이야.."

    주인공 "나 여기로 전학왔어.."

    미소 "진짜? 그럼 우리 같은 학교 다니게 됐네! 대박!"

    미소 "그러면 여기서 멍 때리지말고 내가 학교 소개시켜줄게!"

    scene library with dissolve

    미소 "이쪽은 도서관이고"

    scene playground with dissolve

    미소 "저쪽은 운동장이야."

    scene bg goingToSchool

    show Miso with dissolve

    미소 "중요한 건 우리 반이야! 같이 가자."

    return


# 플레이어 이름 받기
label get_player_name: 
    $ protagonist_name = renpy.input("당신의 이름은 무엇인가요? (2글자 이상 입력해주세요)")
    if not protagonist_name or len(protagonist_name) < 2:
        "이름은 2글자 이상으로 입력해주세요."
        jump get_player_name