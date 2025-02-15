image bg playerInput = 'images/bg/init_player.png'

# 플레이어 이름 정의
label init_player_name:
    stop music fadeout 1
    # 플레이어 이름 입력 화면
    scene bg playerInput with fade

    $ protagonist_name = renpy.input("너의 이름을 알려줘! (2글자 이상 입력해주세요)")
    if not protagonist_name or len(protagonist_name) < 2:
        "이름은 2글자 이상 가능합니다."
        jump init_player_name
    jump get_player_name  # 이름 입력 후 get_player_name으로 이동

label get_player_name:
    $ josa = get_josa(protagonist_name, '이가')
    menu:
        "너의 이름이 [protagonist_name][josa] 맞지?"
        "응, 맞아.":
            $ josa = get_josa(protagonist_name, '으로')
            "[protagonist_name][josa] 게임을 계속 시작합니다."
            jump chapter1_start        
        "아니, 다시 알려줄게.":
            jump init_player_name
