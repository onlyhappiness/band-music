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


# 게임에서 사용할 캐릭터를 정의합니다.
define c = Character('예나', color="#c8ffc8")
define s = Character('수연', color="#c8ffc8")
define n = Character('누리', color="#c8ffc8")

define fastdissolve = Dissolve(0.2)
define veryfastdissolve = Dissolve(0.1)
define slowdissolve = Dissolve(1.0)
define slowfade = Fade(0.6, 0.6, 0.6, color="#000000")
define flash = Fade(.01, 0.0, .18, color="#ffffff")
define sshake = Shake((0, 0, 0, 0), 0.3, dist=15)
define sshake2 = Shake((0, 0, 0, 0), 1.0, dist=15)

default loadVersion = "0.1"

# 여기에서부터 게임이 시작합니다.
label start:
    $ loadVersion = "0.1"

    # show text _("{size=65}")

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    jump about

label about:
    show text _("{size=65}")
    e "버전 0.1"
    jump preferences


label preferences:
    show text _("{size=65}")
    e "옵션"
    jump save

label save:
    show text _("{size=65}")
    e "저장"
    jump load

label load:
    show text _("{size=65}")
    e "불러오기"
    jump quit

label quit:
    show text _("{size=65}")
    e "또 기다릴게!"
    return

