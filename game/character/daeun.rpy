# 다은 첫 만남
label daeun_part_1:
    scene black with fade
    window hide
    scene black with flash
    pause 1
    scene black with flash
    pause 1

    "저기... 전학생, 잠깐 괜찮아?"

    scene bg school_classroom with fade
    show daeun_1 at center with fade

    p "나는 살짝 놀라 고개를 들었다."
    "단정한 단발머리, 반듯한 자세의 여학생이 내 책상 옆에 서 있다."
    "부드럽고 차분한 미소가 어딘가 부담스럽지 않다."

    show daeun_1 at left with move
    window show
    "..."
    menu:
        "...응, 괜찮아.": # 긍정
            # return
            "...응, 괜찮아."

        "(조용히 고개만 끄덕인다.)": # 평범한 반응
            # return
            "(조용히 고개만 끄덕인다.)"

        "무슨 일이야?": # 경계
            # return
            "무슨 일이야?"

    window auto
    
    show daeun_1 at center with move
    de "나는 다은이라고 해. 이 반의 반장이야."
    de "혹시 불편한 건 없나 해서."

    p "...괜찮아."

    de "그래? 다행이다."
    de "전학 첫 날이면 좀 낯설 수 있으니까."
    "다은은 잠시 머뭇거리다가 나를 바라보며 말을 이어갔다."
    de "혹시 자리 불편하지 않아? 창가 쪽이라 빛이 너무 들어오는 건 아닌가 해서."

    window show
    menu: 
        "빛이 따뜻해서 괜찮아.": # 긍정
            # return
            "빛이 따뜻해서 괜찮아."

        "...아무래도 신경 안 써.": # 부정
            # return
            "...아무래도 신경 안 써."

    window auto

    de "응, 그렇구나. 난 햇살이 눈부셔서 창가 쪽은 잘 못 앉거든."
    de "근데 너한테는 잘 어울리는 것 같아."

   
    return
