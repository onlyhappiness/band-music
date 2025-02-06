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
    p "..."
    pause 0.5
    show bg yena_appear_1 with fade
    pause 0.7
    p "..."

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
            y "그래, 너 딱 보니까 맞네~"
        "아니.":
            p "아니요. 사람 잘못 보셨어요."
            y "아니, 너! 딱 보니까 맞네!"

    y "아, 반가워. 난 유나라고 해."
    y "밴드부에서 기타치고 있어."
    p "..."
    y "저번에 너 락 페스티벌에서 봤어. 기타 엄청 잘 치더라?"
    "[p]는 순간 얼어붙는다. 예상치 못한 질문에 당황하며 시선을 피한다."
    show bg memory_1 with flash
    pause 0.5
    p "윽..."
    play sound "audio/se/camera 1.wav"
    show bg memory_2 with flash
    pause 0.5
    p "..."
    play sound "audio/se/camera 1.wav"
    show bg memory_3 with flash
    pause 0.5
    p "...아니야..."
    scene black
    pause 0.7
    scene bg school_classroom with fade
    p "..."
    p "...사람 잘못 봤어..."
    show yena_1 at center with dissolve
    y "에이~ 말도 안 돼. 그런 말로 속일 수 있을 거 같아?"
    y "기타 잡은 손은 금방 알아보니까~"
    p "..."
    "그녀는 내 손을 힐끔 쳐다보며 장난스럽게 웃는다."
    "나는 순간 손을 움켜쥐었다."
    pause 0.3
    p "..."
    menu:
        "아무 말 없이 손을 감춘다.": # 회피
            p "..."

        "기타 같은 거 안 쳐.":
            p "..."
            p "기타 같은 거 안 쳐."
            hide yena_1
            show yena_2 at center with dissolve
            y "흐음~ 그렇게 말하면 더 수상한데?"

    hide yena_1
    hide yena_2
    show yena_3 at center with dissolve
    y "뭐. 괜찮아. 진실은 언젠가 밝혀지는 법이니까!"
    pause 0.5
    hide yena_3
    show yena_1 at center with dissolve
    y "방과 후 음악실로 와. 그냥 구경만 해도 돼."
    y "근데 솔직히 구경만 하고 가긴 힘들걸?"
    p "..."
    hide yena_1
    show yena_a at center with dissolve
    pause 0.3
    show yena_a at right with move
    pause 0.5
    hide yena_a with dissolve
    "나는 대답할 틈도 없이 활발했던 유나는 손을 흔들며 돌아선다..."
    p "..."
    "그러다 유나는 갑자기 멈춰서 뒤돌아본다."
    show yena_2 at center with dissolve
    pause 0.3
    y "근데 있잖아-"
    y "진짜 기타 안 치는거면, 왜 그렇게 당황한거야?"
    pause 0.5
    "순간 움찔하며 고개를 돌렸다."
    hide yena_2
    pause 0.2
    show yena_1 at center with dissolve
    "유나는 장난스럽지만 진지하게 나를 보고 있다."
    menu:
        "당황한 거 아니야.":
            p "..."
            p "당황한 거 아니야."
        "네가 너무 시끄러워서 그래.":
            p "네가 너무 시끄러워서 그래."
    hide yena_1
    pause 0.2
    show yena_3 at center with dissolve
    y "하하! 진짜 웃기네. 너 재밌다."
    pause 0.2
    hide yena_3
    pause 0.2
    show yena_1 at center with dissolve
    y "근데~ 너 같은 애일수록 더 궁금해진다고~"
    pause 0.2
    "유나는 내 책상 위에 기타 픽을 살짝 올려놓는다."
    pause 0.2
    hide yena_1
    show yena_3 at center with dissolve
    y "이거, 선물!"
    y "혹시 모르잖아. 언젠가 필요할지도?"
    "그렇게 말하고 유나는 다시 돌아서지만, 마지막 한 마디를 남겼다."
    hide yena_3
    pause 0.1
    show yena_a at center with dissolve
    y "안 와도 상관없어. 근데, 안 오면 더 신경 쓰일걸?"
    "유나의 말에 나는 말없이 픽을 바라보았다."
   
    return
   
    
