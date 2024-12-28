# 이 파일에 게임 스크립트를 입력합니다.
init python:
    import pygame

    def green_tag(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color={}".format("#00a206")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    def blue_tag(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color={}".format("#65afda")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    def red_tag(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color={}".format("#d01807")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
        ]
    def white_tag(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color={}".format("FFFFFF")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
        ]
    def gold_tag(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color={}".format("#ffd700")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    def autograph_tag(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"font={}".format("auto.otf")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["red"] = red_tag
    config.custom_text_tags["blue"] = blue_tag
    config.custom_text_tags["green"] = green_tag
    config.custom_text_tags["white"] = white_tag
    config.custom_text_tags["gold"] = gold_tag
    config.custom_text_tags["auto"] = autograph_tag

image bg quit_bg = 'images/bg/quit_bg.png'

define flash = Fade(.01, 0.0, .18, color="#ffffff")


# 게임에서 사용할 캐릭터를 정의합니다.
define p = Character("[protagonist_name]", color="#ffffff")

define t = Character('선생님', color="#ffffff")
define c = Character('예나', color="#ffffff")
define s = Character('수연', color="#ffffff")
define n = Character('누리', color="#ffffff")
define tg = Character('태구', color="#ffffff")


default loadVersion = "0.1"

# 여기에서부터 게임이 시작합니다.
label start:
    $ loadVersion = "0.1"

    jump init_player_name

label quit:
    scene bg quit_bg with fade

    show text _("{size=65}")
    c "{cps=10}또.. 기다릴게..!{/cps}"
    return

