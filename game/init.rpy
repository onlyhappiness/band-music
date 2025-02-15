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
    
    def get_josa(name, josa_type):
        """
        한글 조사 처리 함수
        """
        JOSA_PAIRS = {
            '은는': ('은', '는'),
            '이가': ('이', '가'),
            '을를': ('을', '를'),
            '과와': ('과', '와')
        }

        if not name or not isinstance(name, str):
            return ""
        
        # 한글의 유니코드 범위 내에서 받침 확인
        code = ord(name[-1]) - 0xAC00

        if code < 0 or code > 11172:
            return JOSA_PAIRS[josa_type][1]  # 한글이 아닌 경우 받침 없는 것으로 처리
            
        has_final = bool(code % 28)
        return JOSA_PAIRS[josa_type][0] if has_final else JOSA_PAIRS[josa_type][1]    

    config.custom_text_tags["red"] = red_tag
    config.custom_text_tags["blue"] = blue_tag
    config.custom_text_tags["green"] = green_tag
    config.custom_text_tags["white"] = white_tag
    config.custom_text_tags["gold"] = gold_tag
    config.custom_text_tags["auto"] = autograph_tag

# image bg quit_bg = 'images/bg/quit_bg.png'

define flash = Fade(.01, 0.0, .18, color="#ffffff")


# 게임에서 사용할 캐릭터를 정의합니다.
define p = Character("[protagonist_name]", color="#000000")

define t = Character('선생님', color="#000000")
define y = Character('예나', color="#F8BBD0")
define s = Character('수연', color="#4682B4")
define n = Character('누리', color="#F0D59C")
define de = Character('다은', color="#D99152")


default loadVersion = "0.1"
