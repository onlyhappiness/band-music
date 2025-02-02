
label test:
    scene black
    # show text _("{color=#ffffff}{size=100}DAY 1{/size}{/color}") with fade
    # pause 2
    scene bg school_classroom with fade
    show yena_1 at center with dissolve


    y "고등학교 정문 앞, 주인공은(은)는 멈춰 서서 학교 건물을 바라보았다."
   
 
    window show 
    narrator "어떻게 소개할까..."

    menu:
        "자신있게 소개하자!":
            "좋아"

        "좀.. 부끄러운데..":
            "좋아"

    window auto
    return

