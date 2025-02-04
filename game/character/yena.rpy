label yena_part_1:
    scene bg school_classroom with fade
    "다은이 자리로 돌아간 뒤, 교실은 평소처럼 떠들석하다."
    # 소리 삽입
    "[p]는 다시 조용히 책상에 엎드려 눈을 감았다."
    scene black with fade
    p "...이제 좀 조용해졌네."
    "..."
    "..."
    y "{size=32}그 전학생이 왔다고 들었는데?{/size}"
    y "{size=32}여기 전학생이 전학 온 반 맞지?!{/size}"

    show bg yena_appear_1 with fade
    # window hide
    # scene black with flash
    # pause 1
    # scene black with flash
    pause 2
    "..."

    "[p]는 생기발랄한 목소리에 화들짝 눈을 떴다."
    "시야가 또렷해지기도 전에, 반짝이는 눈동자가 가까이 다가왔다."
    "그녀는 [p]의 책상 옆에 몸을 기울이며, 해맑은 미소를 띤 채 [p](을)를 내려다보았다."

    show bg yena_appear_2 with fade

    y "{size=32}전학생, 너 맞지?{/size}"
    "그녀는 마치 나를 알아본 사람처럼 자연스럽게 말을 걸어왔다."
    "..."
    menu:
        "...나?":
            p "...나?"
            y "그래, 너 맞잖아!"
        "아니.":
            p "아니요. 사람 잘못 보셨어요."
            y "아니, 너 맞잖아!"

    y "그 때 락 페스티벌에서 봤어. 기타 엄청 잘 치더라?"
    "[p]는 순간 얼어붙는다. 예상치 못한 말에 당황하며 시선을 피한다."
    show bg memory_1 with flash
    pause 0.5
    play sound "audio/se/camera 1.wav"
    show bg memory_2 with flash
    pause 0.5
    play sound "audio/se/camera 1.wav"
    show bg memory_3 with flash
    pause 2
    scene black
    pause 1.5
    scene bg school_classroom with fade
    p "..."
    p "...사람 잘못 본 거 같은데."
    show yena_1 at center with dissolve

    y "에이~ 말도 안 돼. 딱 보니까 너던데?"
    y "기타 잡은 손은 금방 알아보니까~"
    "..."
    "그녀는 내 손을 힐끔 쳐다보며 장난스럽게 웃는다."
    "나는 순간 손을 움켜쥔다."

    return
   
    
