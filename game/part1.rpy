image bg school_gate = 'images/bg/start_part_1.png'
image bg school_classroom = 'images/bg/classroom_1.png'

# 아침의 시작: 평범한 첫걸음
label start_part1:
    scene bg school_gate with fade

    "{green}{cps=10}아침의 시작{/cps}{/green}"

    "{blue}{cps=20}고등학교 정문 앞, [p] 은(는) 멈춰 서서 학교 건물을 바라보았다.{/cps}{/blue}"
    "{blue}{cps=20}학생들이 활기차게 웃고 떠들며 등교하는 모습이 보이지만, 그는 혼자 그 모습을 지켜보았다.{/cps}{/blue}"
    "{blue}{cps=20}평범한 가방을 멘 [p]의 손은 약간 굳어 있었다.{/cps}{/blue}"
    p "{blue}{cps=20}여기도 별 다른 건 없겠지...{/cps}{/blue}"
    p "{blue}{cps=20}그냥 무난하게.. 조용히 지내고 싶어..{/cps}{/blue}"
    "{blue}{cps=20}학생들 사이로 천천히 걸음을 옮기는 [p].{/cps}{/blue}"
    "{blue}{cps=20}몇몇 학생들이 낯선 얼굴을 힐끔 쳐다보지만, 주인공은 신경 쓰지 않으려 애썼다.{/cps}{/blue}"

# 교무실
    # "{green}{cps=10}교무실{/cps}{/green}"

    
# 교실로 들어가다
    scene bg school_classroom with fade

    "{green}{cps=10}교실{/cps}{/green}"

    "{blue}교실 문을 열자 교실 안이 순간 조용해졌다.{/blue}"
    "{blue}모두가 전학생인 [p] 에게 시선을 모았다.{/blue}"
    t "{cps=20}자, 얘들아. 오늘 새로 전학 온 친구가 있어.{/cps}"
    t "{cps=20}자, [p] 자기 소개해볼래?{/cps}"

    # 소개할까?

    t "{cps=20}다들 잘 지내보도록 해.{/cps}"
    "{blue}{cps=20}선생님은 분위기를 가볍게 넘기며 조용히 교실을 둘러보았다.{/cps}{/blue}"
    t "{cps=20}그러면 음.. 빈자리가 저기 창가쪽에 있네.{/cps}"

    # 자리 zoom in
    "{blue}{cps=20}[p] (은)는 조용히 자리에 앉아 가방을 내려놓았다.{/cps}{/blue}"
    "{blue}{cps=20}창문 밖으로 쏟아지는 햇살이 눈부시게 느껴져 잠깐 창밖을 바라보았다.{/cps}{/blue}"
    p "{blue}{cps=20}...그냥 무난히 지내고 싶은데{/cps}{/blue}"


# 태구와 첫 대화


# 첫날의 여운
