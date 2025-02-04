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

    "나는 살짝 놀라 고개를 들었다."
    "단정한 단발머리, 반듯한 자세의 여학생이 내 책상 옆에 서 있다."
    "부드럽고 차분한 미소가 어딘가 부담스럽지 않다."

    window show
    "..."

    de "잠깐 시간 괜찮아?"
    menu:
        "응, 괜찮아.": # 긍정
            p "응, 괜찮아."

        "(조용히 고개만 끄덕인다.)": # 평범한 반응
            "(조용히 고개만 끄덕인다.)"

        "무슨 일이야?": # 경계
            p "무슨 일이야?"
    
    de "반가워. 나는 다은이라고 해. 이 반의 반장이야."
    de "음... 혹시 불편한 건 없나 해서."
    p "...괜찮아."
    de "그래? 다행이다."
    de "전학 첫 날이면 좀 낯설 수 있으니까."
    "다은은 잠시 머뭇거리다가 나를 바라보며 말을 이어갔다."
    de "혹시 자리 불편하지 않아? 창가 쪽이라 빛이 너무 들어오는 건 아닌가 해서."

    window show
    menu: 
        "빛이 따뜻해서 괜찮아.": # 긍정
            # return
            p "빛이 따뜻해서 괜찮아."
            de "응, 그렇구나. 난 햇살이 눈부셔서 창가 쪽은 잘 못 앉거든."
            de "근데 너한테는 잘 어울리는 것 같아."

        "...아무래도 신경 안 써.": # 부정
            # return
            p "...아무래도 신경 안 써."
            de "응, 그렇구나. 난 햇살이 눈부셔서 창가 쪽은 잘 못 앉거든."
            de "근데 너한테는 잘 어울리는 것 같아."
            "다은은 [p]가 불편하지 않게 자연스럽게 웃으며 넘어간다."

    p "......"
    hide daeun_1
    show daeun_2 at center with dissolve
    pause 2
    de "......"
    "잠시 어색한 침묵."
    "그러나 다은은 침묵을 어색해지지 않고 조용히 책상에 손을 얹으며 말을 이어가려고 한다."
    hide daeun_2
    show daeun_1 at center with dissolve
    "그녀의 시선이 자연스럽게 내 손끝으로 향한다."
    "책상 모서리를 무의식적으로 '톡톡' 두드리고 있던 내 손가락."
    hide daeun_1
    show daeun_4 at center with dissolve
    de "...혹시 리듬 타고 있었어?"
    "나는 움찔하며 손을 움켜쥐었다."
    p "그냥... 습관이야."
    de "아, 그래? 나는 펜돌리는 습관이 있어서."
    de "괜히 손이 가만히 있질 못하거든."
    hide daeun_4
    show daeun_1 at center with dissolve
    pause 1.5
    "다은은 대수롭지 않게 웃으며 넘긴다."
    "그 웃음은 억지로 친한 척하려는 게 아닌, 편안한 분위기를 만들려는 듯한 느낌이 들었다."

    menu: 
        "...넌 말 잘하네.": # 긍정
            p "...넌 말 잘하네."
            jump daeun_part_1A_1

        "(아무 말 없이 시선을 피한다.)": # 평범 
            "(아무 말 없이 시선을 피한다.)"
            jump daeun_part_1A

        "굳이 이렇게 친한 척 할 필요는 없어.":  # 부정 
            p "굳이 이렇게 친한 척 할 필요는 없어."
            jump daeun_part_1A

    return


# 선택지 공통
label daeun_part_1A:
    show daeun_2 at center with dissolve
    de "반장이라서 그런가봐. 그냥 익숙해진 것 같아."
    de "불편했다면 미안..."
    "다은은 잠시 창밖을 바라보다가 작게 웃으며 말을 덧붙였다."
    hide daeun_2
    show daeun_1 at center with dissolve
    de "혹시 나중에 도움이 필요하면 꼭 말해줘."
    "다은은 마지막으로 부드럽게 인사를 하고 자리로 돌아갔다."

    jump yena_part_1

    return 
   
# 선택지 긍정
label daeun_part_1A_1:
    hide daeun_1
    show daeun_2 at center with dissolve
    de "그냥 말 안하면, 더 낯설잖아..."
    de "난 전학 왔을 때 아무도 말 안 걸어줬거든... 그때 진짜 외로웠어."
    hide daeun_2
    show daeun_1 at center with dissolve
    "다은은 잠시 창밖을 바라보다가 작게 웃으며 말을 덧붙였다."
    de "그래서인지, 전학생 보면 괜히 신경 쓰이더라고."
    "어쩌면... 그녀의 친절은 억지가 아니었을지도 모른다."

    menu:
        "... 고마워.":
            p "... 고마워."
            hide daeun_1
            show daeun_3 at center with dissolve

        "(고개를 끄덕이며 조용히 미소를 짓는다.)":
            "(고개를 끄덕이며 조용히 미소를 짓는다.)"

    de "별거 아니야. 그냥 같은 반이니까 그런거지."
    de "혹시 나중에 도움이 필요하면 꼭 말해줘. 반장 특권으로 도와줄테니까."
    "다은은 마지막으로 부드럽게 인사를 하고 자리로 돌아갔다."
    jump yena_part_1

    return
