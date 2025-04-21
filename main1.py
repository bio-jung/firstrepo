# MBTI 성격별 특징을 간단히 조회할 수 있는 코드

def get_mbti_traits(mbti_type):
    mbti_traits = {
        "INTJ": "전략가 - 독립적이며 분석적인 성격",
        "INTP": "논리학자 - 호기심 많고 이론적 사고",
        "ENTJ": "통솔자 - 리더십 강하고 목표 지향적",
        "ENTP": "변론가 - 창의적이고 대화에 능숙",
        "INFJ": "옹호자 - 통찰력 있고 조용한 비전가",
        "INFP": "중재자 - 이상주의자이며 깊은 감정 소유자",
        "ENFJ": "선도자 - 타인을 이끄는 카리스마 소유자",
        "ENFP": "활동가 - 열정적이며 자유로운 영혼",
        "ISTJ": "관리자 - 신중하고 책임감 있는 성격",
        "ISFJ": "수호자 - 헌신적이고 성실한 보호자",
        "ESTJ": "경영자 - 실용적이고 조직적",
        "ESFJ": "집정관 - 사교적이고 협조적인 성격",
        "ISTP": "장인 - 실용적이며 유연한 문제 해결사",
        "ISFP": "모험가 - 감성적이고 자유로운 영혼",
        "ESTP": "사업가 - 에너지 넘치고 솔직한 유형",
        "ESFP": "연예인 - 외향적이고 즉흥적인 성격"
    }

    mbti_type = mbti_type.upper()
    return mbti_traits.get(mbti_type, "존재하지 않는 MBTI 유형입니다.")


if __name__ == "__main__":
    user_input = input("MBTI 유형을 입력하세요 (예: INTJ): ")
    result = get_mbti_traits(user_input)
    print(f"[{user_input}] 특징: {result}")
