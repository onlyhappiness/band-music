label chapter1_start:
    scene bg school_gate with fade
    play music "audio/bgm/walking_school.ogg"
    "고등학교 정문 앞, [p](은)는 멈춰 서서 학교 건물을 바라보았다."
    "학생들이 활기차게 웃고 떠들며 등교하는 모습이 보이지만, 그는 혼자 그 모습을 지켜보았다."
    "평범한 가방을 멘 [p]의 손은 약간 굳어 있었다."
    p "여기도 별 다른 건 없겠지..."
    p "그냥 무난하게.. 조용히 지내고 싶어.."
    "학생들 사이로 천천히 걸음을 옮기는 [p]."
    "몇몇 학생들이 낯선 얼굴을 힐끔 쳐다보지만, [p](은)는 신경 쓰지 않으려 애썼다."


label chapter1_teacher_first_meeting:
    # 교무실 밖
    "잔뜩 긴장한 채로 교무실 앞에 멈춰 섰다."
    p "괜찮아... 그냥 들어가면 돼."
    "[p]는 스스로 다독이면서 교무실 문을 열었다."

    # 교무실
    p "실례합니다..."
    "작게 중얼거리며 교무실 문을 조심스럽게 열었다."
    ""


label chapter1_classroom_start:
    scene black with fade
    window hide
    scene bg school_classroom with fade
    pause 1

    stop music fadeout 1
    play music "audio/se/close_classroom.ogg"
    stop music fadeout 1

    "교실 문을 열자 교실 안이 순간 조용해졌다."
    "모두가 전학생인 [p]에게 시선을 모았다."
    show teacher at center with dissolve
    t "자, 얘들아. 오늘 새로 전학 온 친구가 있어."
    t "자, [p]아 자기 소개해볼래?"
    show teacher at left with move

    # 소개할까?
    "(어떻게 소개하지...)"
    window show 
    menu:
        "나를 소개하자.":
            p "안녕... 나는 [p] 라고 해.. 앞으로 잘 부탁해."
            show teacher at center with move
            t "좋아. 다들 잘 지내보도록 해."
            
        "좀.. 부끄러운데..":
            p "...음, 잘 부탁해."
            show teacher at center with move
            t "다들 잘 지내보도록 해."
            "선생님은 분위기를 가볍게 넘겼다."

    t "그러면.. 음.."
    "선생님은 조용히 교실을 둘러보았다."
    t "빈자리가 저기 창가쪽에 있네."
    t "이제 [p]는 저 자리 앉아서 수업 들으면 된단다."

    hide teacher with dissolve
    pause 1
    # 자리 zoom in
    "[p](은)는 조용히 자리에 앉아 가방을 내려놓았다."
    "창문 밖으로 쏟아지는 햇살이 눈부시게 느껴져 잠깐 창밖을 바라보았다."

    p "...그냥 무난히 지내고 싶은데"
