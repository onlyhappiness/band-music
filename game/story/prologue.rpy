image bg playerInput = 'images/bg/init_player.png'

# 플레이어 이름 정의
label init_player_name:
    stop music fadeout 1
    # 플레이어 이름 입력 화면
    scene bg playerInput with fade

    $ protagonist_name = renpy.input("너의 이름을 알려줘! (2글자 이상 입력해주세요)")
    $ protagonist_name = protagonist_name.strip()  # 앞뒤 공백 제거
    $ protagonist_name = protagonist_name.replace(" ", "")  # 중간 공백 제거
    
    if not protagonist_name or len(protagonist_name) < 2:
        "이름은 2글자 이상 가능합니다."
        jump init_player_name

    if not is_hangul(protagonist_name):
        "제대로 된 이름을 입력해주세요."
        jump init_player_name
        
    jump get_player_name  # 이름 입력 후 get_player_name으로 이동

label get_player_name:
    $ 이가 = get_이가(protagonist_name)
    $ 으로 = get_으로(protagonist_name)

    menu:
        "너의 이름이 [protagonist_name][이가] 맞지?"
        "응, 맞아.":
            "[protagonist_name][으로] 게임을 계속 시작합니다."
            jump chapter1_start        
        "아니, 다시 알려줄게.":
            jump init_player_name
