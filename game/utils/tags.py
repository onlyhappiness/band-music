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
            (renpy.TEXT_TAG,u"/font"),
        ]
