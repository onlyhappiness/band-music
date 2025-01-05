# define config.default_cps = 20

# 아침의 시작: 평범한 첫걸음
label start_part_1:
    scene black
    show text _("{color=#ffffff}{size=100}DAY 1{/size}{/color}") with fade
    pause 2

    scene bg school_gate with fade

    play music "audio/bgm/walking_school.ogg"

    "{size=25}고등학교 정문 앞, [p](은)는 멈춰 서서 학교 건물을 바라보았다.{/size}"
    "{size=25}학생들이 활기차게 웃고 떠들며 등교하는 모습이 보이지만, 그는 혼자 그 모습을 지켜보았다.{/size}"
    "{size=25}평범한 가방을 멘 [p]의 손은 약간 굳어 있었다.{/size}"
    p "{size=25}여기도 별 다른 건 없겠지...{/size}"
    p "{size=25}그냥 무난하게.. 조용히 지내고 싶어..{/size}"
    "{size=25}학생들 사이로 천천히 걸음을 옮기는 [p].{/size}"
    "{size=25}몇몇 학생들이 낯선 얼굴을 힐끔 쳐다보지만, [p](은)는 신경 쓰지 않으려 애썼다.{/size}"

    jump class_room_part_1

# 교실로 들어가다
label class_room_part_1:
    scene black with fade
    window hide
    scene bg school_classroom with fade

    "{green}{cps=10}교실{/size}{/green}"
    stop music fadeout 1
    play music "audio/se/close_classroom.ogg"
    stop music fadeout 1

    "{size=25}교실 문을 열자 교실 안이 순간 조용해졌다.{/size}"
    "{size=25}모두가 전학생인 [p]에게 시선을 모았다.{/size}"

    show teacher at center with dissolve

    t "{size=25}자, 얘들아. 오늘 새로 전학 온 친구가 있어.{/size}"
    t "{size=25}자, [p]아 자기 소개해볼래?{/size}"

    # 소개할까?
    menu:
        "자신있게 소개하자!":
            p "{size=25}안녕! 내 이름은 [p]야. 잘 부탁해!{/size}"
            t "{size=25}좋아. 다들 잘 지내보도록 해.{/size}"
            "{size=25}선생님은 분위기를 가볍게 넘기며 조용히 교실을 둘러보았다.{/size}"

        "좀.. 부끄러운데..":
            p "{size=25}안녕.. 나는 [p] 라고 해.. 앞으로 잘 부탁해..{/size}"
            t "{size=25}좋아. 다들 잘 지내보도록 해.{/size}"
            "{size=25}선생님은 분위기를 가볍게 넘기며 조용히 교실을 둘러보았다.{/size}"

            
        "...":
            p "{size=25}...{/size}"
            "{size=25}...{/size}"
            t "{size=25}다들 잘 지내보도록 해.{/size}"
            "{size=25}선생님은 분위기를 가볍게 넘기며 조용히 교실을 둘러보았다.{/size}"

    t "{size=25}그러면 음.. 빈자리가 저기 창가쪽에 있네.{/size}"

    # 자리 zoom in
    "{size=25}[p](은)는 조용히 자리에 앉아 가방을 내려놓았다.{/size}"
    "{size=25}창문 밖으로 쏟아지는 햇살이 눈부시게 느껴져 잠깐 창밖을 바라보았다.{/size}"
    p "{size=25}...그냥 무난히 지내고 싶은데{/size}"

    jump taegu_part_1

# 태구와 첫 대화
label taegu_part_1:
    scene black with fade
    window hide
    scene black with flash
    pause 1
    scene black with flash
    pause 1
    "야, 전학생. 자는거야?"
    scene bg school_classroom with fade
    p "{size=25}아무 생각 없이 멍때리고 있던 [p](은)는 책상에 엎드려 자고 있었다.{/size}"
    "{size=25}[p](은)는 살짝 찡그리며 고개를 들었다.{/size}"
    show taegu_1 at center with fade
    play sound "audio/bgm/taegu.mp3"
    "{size=25}흐릿한 눈으로 옆자리를 보니, 이상한 선글라스를 쓴 남학생이 그를 바라보고 있다.{/size}"

    tg "{size=25}전학 첫 날에 바로 잔다니.. 너도 대단하네{/size}"
    tg "{size=25}이제 점심시간이라 밥 먹자고 깨웠어.{/size}"
    tg "{size=25}반가워. 난 태구라고 해.{/size}"
    p "{size=25}뭐지...? 저 슬라임은...{/size}"
    "{size=25}[p] (은)는 순간 당황했지만, 곧 고개를 살짝 끄덕였다.{/size}"
    p "{size=25}아... 어. 반가워.{/size}"
    tg "{size=25}내가 관상을 좀 볼 줄 알거든.{/size}"
    tg "{size=25}너 애니메이션 좋아해?{/size}"
    tg "{size=25}내가 요즘 만화를 그리고 있는데{/size}"
    "{size=25}태구는 핸드폰을 꺼내 화면을 보여주었다.{/size}"
    tg "{cps=60}여기 만화 주인공이 나인데 여자한테 관심 없는 약간 <미소년 부잣집 도련님> 느낌이랄까나?{/size}"
    tg "{cps=60}근데 이제 <여자 메이드>가 나를 좋아해가지고 근데 이제 내가 좀 귀찮아하는데 계속 나한테 애원하는거야.{/size}"
    tg "{cps=60}그렇지만 나는!{/size}"
    tg "{cps=60}그런 거에 신경쓰지 않고 이 세계를 구하기 위한 <용사> 역할이어서 열심히 해야하는 부분인데{/size}"
    tg "{cps=60}어쨌든 내가 위험에 빠지자 메이드가 나를 구해주는 내용이야{/size}"
    tg "{size=25}알겠지?{/size}"
    "{size=25}[p](은)는 다시 한 번 당황했지만, 태구는 대답을 기다리지도 않고 말을 이어갔다.{/size}"
    tg "{cps=60}그래서 내가 메이드에게 너의 정체가 뭐냐고 물어볼텐데 여기서 진짜 중요한 대사가 나오거든?{/size}"
    tg "{cps=60}잊으셨어요.. 용사님? 저에요. 라고 메이드가 대답하는거야.{/size}"
    p "{size=25}...{/size}"
    tg "{size=25}아, 이게 아닌가? 혹시 애니 음악을 좋아해?{/size}"
    tg "{size=25}나 애니 오프닝 엄청 좋아하거든.{/size}"
    "{size=25}다시 태구는 핸드폰을 꺼내 화면을 보여주었다.{/size}"
    tg "{cps=60}혹시 <비스크돌> 오프닝 알아?{/size}"
    p "{size=25}...{/size}"
    tg "{cps=60}그러면, <소드 아트 온라인> 오프닝 알아?{/size}"
    p "{size=25}...{/size}"
    tg "{cps=60}그러면... <방패 용사 성공담> 오프닝 알아?{/size}"
    p "{size=25}...모르겠어{/size}"
    tg "{cps=60}그러면... <청춘돼지는 바니걸 선배의 꿈을 꾸지 않는다> 오프닝 알아?{/size}"
    p "{size=25}아니... 몰라..{/size}"
    tg "{cps=60}그러면! <최애의 아이> 오프닝 알아?{/size}"
    p "{size=25}그건.. 알아..{/size}"
    tg "{cps=60}그러면...! <B코마치> 알아?{/size}"
    p "{size=25}그건... 몰라...{/size}"
    tg "{size=25}이 노래 진짜 좋아. 너도 한 번 들어봐. 딱 내 스타일이야.{/size}"
    "{size=25}[p](은)는 태구가 보여준 핸드폰 화면을 흘깃 보며 피식 웃었다.{/size}"
    "{size=25}태구의 열정이 재미있게 느껴지기 시작했다.{/size}"
    p "{size=25}애니 노래는 잘 몰라... 그냥 음악은 조금 들을 때가 있긴 했어.{/size}"

    # 주인공 기억 회상
    scene black with fade
    window hide
    # 여기에 배경음악 삽입
    # play sound "audio/bgm/bgm_1.mp3"
    play sound "audio/se/camera 1.wav"
    show bg memory_1 with flash
    pause 0.5
    play sound "audio/se/camera 1.wav"
    show bg memory_2 with flash
    pause 0.5
    play sound "audio/se/camera 1.wav"
    show bg memory_3 with flash
    pause 2
    p "{size=25}(근데 음악을 다시 하진 않을 거야..){/size}"
    scene black
    scene bg school_classroom with fade
    pause 1.5

    # 태구 대사
    show taegu_1 at center with dissolve
    tg "{size=25}...{/size}"
    tg "{size=25}그러니까 좋아하는 애니는 있는거지?{/size}"

    p "{cps=10}.....{/size}"
    "{size=25}[p](은)는 다시 책상에 팔을 베고 엎드려 눈을 감았다.{/size}"

    scene black with fade
    jump yuna_part_1

# 예나의 등장
label yuna_part_1:
    scene black with fade
    pause 0.5
    y "{size=25}그 전학생이 왔다고 들었는데?{/size}"
    y "{size=25}여기 전학생이 전학 온 반 맞지?!{/size}"
    window hide
    scene black with flash
    pause 1
    scene black with flash
    pause 2

    show bg yena_appear_1 with fade
    play sound "audio/bgm/yena.ogg"

    "{size=25}[p](은)는 생기발랄한 목소리에 화들짝 눈을 떴다.{/size}"
    "{size=25}시야가 또렷해지기도 전에, 반짝이는 눈동자가 가까이 다가왔다.{/size}"
    "{size=25}그녀는 [p]의 책상 옆에 몸을 기울이며, 해맑은 미소를 띤 채 [p](을)를 내려다보았다.{/size}"

    show bg yena_appear_2 with fade

    y "{size=25}너 맞지? 저번 락 페스티벌에서 상 받았던 애!{/size}"
    "{size=25}[p](은)는 그녀의 말에 당황하며 얼굴을 빨개졌다.{/size}"
    p "{size=25}...락 페스티벌? {/size}"
    y "{size=25}내가 그때 바로 앞에서 봤거든. 진짜 멋있었어. 그 솔로 연주! 너잖아?{/size}"
    "{size=25}발랄한 그녀는 미소를 띠며 눈을 바라보았다.{/size}"
    "{size=25}[p](은)는 말을 잇지 못하고 고개를 피하며 어색하게 대답했다.{/size}"

    p "{size=25}...아니야. 사람 잘못 본 거야.{/size}"

    window hide
    show bg school_classroom with fade
    show yena_1 at center with dissolve

    y "{size=25}뭐야? 내가 딱 봤는데? 네 얼굴이 똑같았어.{/size}"
    y "{size=25}그리고 그 기타 연주... 아무나 할 수 있는 게 아니던데.{/size}"
    y "{size=25}그러니까 너 맞지?{/size}"

    p "{size=25}...{/size}"
    p "{size=25}이제 그런 건 옛날 얘기야. 지금은 기타 치지도 않고, 앞ㅡ로도 안 칠거야...{/size}"

    y "{size=25}왜? 그런 재능을 왜 묻어둬? 그냥 취미로라도 하면 되잖아.{/size}"
    p "{size=25}...관심없어.{/size}"

    "{size=25}그녀는 [p]의 태도에 당황하기는커녕, 오히려 더 흥미로워진 듯 [p]에게 다가섰다.{/size}"
    hide yena_1 with dissolve
    show yena_2 at center with dissolve
    y "{size=25}이상하네..? 그런 표정으로 관심 없다고 말하면 누가 믿어?{/size}"
    y "{size=25}너 사실 다시 음악하고 싶어 하는 거 아니야?{/size}"

    "{size=25}[p](은)는 그녀의 말에 움찔하며 눈길을 피했다. 왠지 그녀의 말이 자신을 꿰뚫어 본 것처럼 느껴졌다.{/size}"
    y "{size=25}흥, 너 거짓말은 못하겠다~{/size}"
    y "{size=25}좋아. 이렇게 하자. 내가 오늘 방과후에 음악실에서 기다릴게.{/size}"
    y "{size=25}네가 와서 한 곡만 연주해주면 넘어가줄게!{/size}"
    p "{size=25}그럴 리 없잖아...{/size}"
    y "{size=25}진짜라니까. 내가 이래뵈도 약속 잘 지키는 사람이라구.{/size}"
    y "{size=25}그럼 약속이야! 방과후에 음악실에서 만나자!{/size}"

    hide yena_2 with dissolve
    stop music fadeout 1
    stop sound fadeout 1

    "{size=25}그녀는 말을 끝내고 미소를 띠며 교실을 나갔다.{/size}"
    jump yuna_leave_1

# 예나가 떠난 뒤
label yuna_leave_1:
    stop music fadeout 1
    scene black with fade
    window hide
    scene bg school_classroom with fade
    "{size=25}한바탕 소란이 지나고, [p](은)는 다시 창 밖을 바라보며 짧게 한숨을 내쉬었다.{/size}"
    p "{size=25}...락 페스티벌이라니. 그걸 알아본 애가 있을 줄이야.{/size}"
    
    play sound "audio/se/camera 1.wav"
    show bg memory_1 with flash
    pause 0.5
    play sound "audio/se/camera 1.wav"
    show bg memory_2 with flash
    pause 0.5
    play sound "audio/se/camera 1.wav"
    show bg memory_3 with flash
    "{size=25}그는 잠시 그 날의 기억에 잠겼다.{/size}"
    "{size=25}수많은 관객들 앞에서 연주하던 순간과, 그 뒤를 따라온 상처가 머릿속을 스친다. 그러나 그는 고개를 저으며 다시 그 기억을 밀어냈다.{/size}"
    scene bg school_classroom with fade
    p "{size=25}지금은 아무 의미 없는데...{/size}"
    tg "{size=25}놀랐지? 원래 저런 애야.{/size}"
    "{size=25}[p](은)는 천천히 고개를 돌려 태구를 보았다. 짧게 한숨을 내쉬며 고개를 끄덕였다.{/size}"
    show taegu_1 at center with fade
    play sound "audio/bgm/taegu.mp3"
    tg "{size=25}방금 너한테 말 걸었던 애는 {gold}예나{/gold}야. 우리 학교에서 모르는 애 없을걸?{/size}"
    tg "{size=25}{gold}밴드부 리더{/gold}인데, 진짜 실력도 대단하고.{/size}"
    tg "{cps=10}...그리고... 예뻐.{/size}"
    "{size=25}[p](은)는 천천히 시선을 창밖으로 돌렸다. 태구는 그런 [p]를 보며 말을 더 이어갔다.{/size}"

    tg "{size=25}그런데 너한테 관심 가지는 거 보니까 신기하네. 보통 저렇게 들이대는 스타일은 아닌데 말이야.{/size}"
    "{size=25}[p](은)는 태구의 말을 듣고도 별다른 반응이 없었다. 그는 무언가 말하려다 이내 고개를 숙였다.{/size}"
    p "{size=25}...그냥 별 일 아닐거야.{/size}"
    tg "{size=25}그래도 이상하단 말이지.. 아까 들어보니까 유나가 락 페스티벌 얘기하던데? 진짜 너 기타 쳤던 거 아니야?{/size}"
    p "{size=25}...그냥 착각했을거야.{/size}"
    "{size=25}[p](은)는 흠칫하며 태구를 보다가 시선을 피하며 대답했다.{/size}"
    tg "{size=25}진짜? 근데, 걔가 그런 그런 착각을 할 애가 아닌데. 특히 음악 쪽으로는 엄청 까다롭거든.{/size}"
    p "{size=25}...{/size}"
    tg "{size=25}음... 그래도 유나가 너한테 관심 가졌다는 거 하나만큼은 확실한데. 조심해.{/size}"
    tg "{size=25}한 번 찍히면 놓는 법이 없는 애니까.{/size}"
    p "{size=25}...{/size}"

    jump develop_intro
