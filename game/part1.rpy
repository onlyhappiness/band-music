image bg school_gate = 'images/bg/start_part_1.png'
image bg school_classroom = 'images/bg/classroom_1.png'

image teacher = 'images/Teacher/teacher_1.png'
image taegu_1 = 'images/Taegu/taegu_1.png'

# 아침의 시작: 평범한 첫걸음
label start_part_1:
    scene bg school_gate with fade

    "{green}{cps=10}아침의 시작{/cps}{/green}"

    "{blue}{cps=20}고등학교 정문 앞, [p](은)는 멈춰 서서 학교 건물을 바라보았다.{/cps}{/blue}"
    "{blue}{cps=20}학생들이 활기차게 웃고 떠들며 등교하는 모습이 보이지만, 그는 혼자 그 모습을 지켜보았다.{/cps}{/blue}"
    "{blue}{cps=20}평범한 가방을 멘 [p]의 손은 약간 굳어 있었다.{/cps}{/blue}"
    p "{blue}{cps=20}여기도 별 다른 건 없겠지...{/cps}{/blue}"
    p "{blue}{cps=20}그냥 무난하게.. 조용히 지내고 싶어..{/cps}{/blue}"
    "{blue}{cps=20}학생들 사이로 천천히 걸음을 옮기는 [p].{/cps}{/blue}"
    "{blue}{cps=20}몇몇 학생들이 낯선 얼굴을 힐끔 쳐다보지만, [p](은)는 신경 쓰지 않으려 애썼다.{/cps}{/blue}"

    jump class_room_part_1

# 교무실
    # "{green}{cps=10}교무실{/cps}{/green}"

    
# 교실로 들어가다
label class_room_part_1:
    scene bg school_classroom with fade

    "{green}{cps=10}교실{/cps}{/green}"

    "{blue}{cps=20}교실 문을 열자 교실 안이 순간 조용해졌다.{/cps}{/blue}"
    "{blue}{cps=20}모두가 전학생인 [p]에게 시선을 모았다.{/cps}{/blue}"

    show teacher at center with dissolve

    t "{cps=20}자, 얘들아. 오늘 새로 전학 온 친구가 있어.{/cps}"
    t "{cps=20}자, [p]야 자기 소개해볼래?{/cps}"

    # 소개할까?
    menu:
        "자신있게 소개하자!":
            p "{cps=20}안녕! 내 이름은 [p]야. 잘 부탁해!{/cps}"
        "좀.. 부끄러운데..":
            p "{cps=20}안녕.. 나는 [p] 라고 해.. 앞으로 잘 부탁해..{/cps}"
        "...":
            p "{cps=20}...{/cps}"

    t "{cps=20}다들 잘 지내보도록 해.{/cps}"
    "{blue}{cps=20}선생님은 분위기를 가볍게 넘기며 조용히 교실을 둘러보았다.{/cps}{/blue}"
    t "{cps=20}그러면 음.. 빈자리가 저기 창가쪽에 있네.{/cps}"

    # 자리 zoom in
    "{blue}{cps=20}[p] (은)는 조용히 자리에 앉아 가방을 내려놓았다.{/cps}{/blue}"
    "{blue}{cps=20}창문 밖으로 쏟아지는 햇살이 눈부시게 느껴져 잠깐 창밖을 바라보았다.{/cps}{/blue}"
    p "{blue}{cps=20}...그냥 무난히 지내고 싶은데{/cps}{/blue}"

    jump taegu_part_1

# 태구와 첫 대화
label taegu_part_1:
    window hide
    scene black with flash
    pause 1
    scene black with flash
    pause 1
    "야, 전학생. 자는거야?"
    scene bg school_classroom with fade
    p "{blue}{cps=20}아무 생각 없이 멍때리고 있던 [p](은)는 책상에 엎드려 자고 있었다.{/cps}{/blue}"
    "{blue}{cps=20}[p](은)는 살짝 찡그리며 고개를 들었다.{/cps}{/blue}"
    show taegu_1 at center with fade
    "{blue}{cps=20}흐릿한 눈으로 옆자리를 보니, 이상한 선글라스를 쓴 남학생이 그를 바라보고 있다.{/cps}{/blue}"

    tg "{cps=20}전학 첫 날에 바로 잔다니.. 너도 대단하네{/cps}"
    tg "{cps=20}이제 점심시간이라 밥 먹자고 깨웠어.{/cps}"
    tg "{cps=20}반가워. 난 태구라고 해.{/cps}"
    "{blue}{cps=20}[p] (은)는 순간 당황했지만, 곧 고개를 살짝 끄덕였다.{/cps}{/blue}"
    p "{cps=20}아... 어. 반가워.{/cps}"
    tg "{cps=20}내가 관상을 좀 볼 줄 알거든.{/cps}"
    tg "{cps=20}너 애니메이션 좋아해?{/cps}"
    tg "{cps=20}내가 요즘 만화를 그리고 있는데{/cps}"
    "{blue}{cps=20}태구는 핸드폰을 꺼내 화면을 보여주었다.{/cps}{/blue}"
    tg "{cps=60}여기 만화 주인공이 나인데 여자한테 관심 없는 약간 <미소년 부잣집 도련님> 느낌이랄까나?{/cps}"
    tg "{cps=60}근데 이제 <여자 메이드>가 나를 좋아해가지고 근데 이제 내가 좀 귀찮아하는데 계속 나한테 애원하는거야.{/cps}"
    tg "{cps=60}그렇지만 나는!{/cps}"
    tg "{cps=60}그런 거에 신경쓰지 않고 이 세계를 구하기 위한 <용사> 역할이어서 열심히 해야하는 부분인데{/cps}"
    tg "{cps=60}어쨌든 내가 위험에 빠지자 메이드가 나를 구해주는 내용이야{/cps}"
    tg "{cps=20}알겠지?{/cps}"
    "{blue}{cps=20}[p](은)는 다시 한 번 당황했지만, 태구는 대답을 기다리지도 않고 말을 이어갔다.{/cps}{/blue}"
    tg "{cps=60}그래서 내가 메이드에게 너의 정체가 뭐냐고 물어볼텐데 여기서 진짜 중요한 대사가 나오거든?{/cps}"
    tg "{cps=60}잊으셨어요? 용사님? 저에요. 라고 메이드가 대답하는거야.{/cps}"
    p "{cps=20}...{/cps}"
    tg "{cps=20}아, 이게 아닌가? 혹시 애니 음악을 좋아해?{/cps}"
    tg "{cps=20}나 애니 오프닝 엄청 좋아하거든.{/cps}"
    "{blue}{cps=20}다시 태구는 핸드폰을 꺼내 화면을 보여주었다.{/cps}{/blue}"
    tg "{cps=60}혹시 <비스크돌> 오프닝 알아?{/cps}"
    p "{cps=20}...{/cps}"
    tg "{cps=60}그러면, <토라도라> 오프닝 알아?{/cps}"
    p "{cps=20}...{/cps}"
    tg "{cps=60}그러면, <소드 아트 온라인> 오프닝 알아?{/cps}"
    p "{cps=20}...{/cps}"
    tg "{cps=60}그러면... <방패 용사 성공담> 오프닝 알아?{/cps}"
    p "{cps=20}...{/cps}"
    tg "{cps=60}그러면... <청춘돼지는 바니걸 선배의 꿈을 꾸지 않는다> 오프닝 알아?{/cps}"
    p "{cps=20}아니... 몰라..{/cps}"
    tg "{cps=60}그러면! <최애의 아이> 오프닝 알아?{/cps}"
    p "{cps=20}그건.. 알아..{/cps}"
    tg "{cps=60}그러면...! <B코마치> 알아?{/cps}"
    p "{cps=20}그건... 몰라...{/cps}"
    tg "{cps=20}이 노레 진짜 좋아. 너도 한 번 들어봐. 딱 내 스타일이야.{/cps}"
    "{blue}{cps=20}[p] (은)는 잠깐 화면을 흘깃 보며 피식 웃었다.{/cps}{/blue}"
    "{blue}{cps=20}태구의 열정이 의외로 재미있게 느껴지기 시작했다.{/cps}{/blue}"
    p "{cps=20}애니 노래는 잘 몰라... 그냥 음악은 조금 들을 때가 있긴 했어.{/cps}"
    

# 첫날의 여운
