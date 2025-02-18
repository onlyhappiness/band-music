# 이 파일에 게임 스크립트를 입력합니다.
init python:
    import pygame

    from utils.hangul import (  # python -> utils로 경로 수정
        is_hangul, 
        get_은는,
        get_이가,
        get_을를,
        get_으로
    )

    # from python.utils.tags import (
    #     green_tag, blue_tag, red_tag, white_tag, gold_tag, autograph_tag
    # )

    # config.custom_text_tags["red"] = red_tag
    # config.custom_text_tags["blue"] = blue_tag
    # config.custom_text_tags["green"] = green_tag
    # config.custom_text_tags["white"] = white_tag
    # config.custom_text_tags["gold"] = gold_tag
    # config.custom_text_tags["auto"] = autograph_tag

# image bg quit_bg = 'images/bg/quit_bg.png'

define flash = Fade(.01, 0.0, .18, color="#ffffff")


# 게임에서 사용할 캐릭터를 정의합니다.
define p = Character("[protagonist_name]",color="#000000")

define t = Character('선생님', color="#000000")
define y = Character('예나', color="#F8BBD0")
define s = Character('수연', color="#4682B4")
define n = Character('누리', color="#F0D59C")
define de = Character('다은', color="#D99152")

default loadVersion = "0.1"


