import streamlit as st

# 질문 및 답변 옵션
questions = [
    {
        "question": "1. 당신은 사람들 사이에서 에너지를 얻는 편인가요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "2. 계획을 세우는 것을 좋아하나요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "3. 새로운 아이디어를 생각하는 것이 흥미로운가요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "4. 타인을 돕는 것을 좋아하나요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "5. 즉흥적인 결정을 잘 내리나요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "6. 감정보다 논리를 더 중시하나요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "7. 상황에 따라 변화를 좋아하나요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "8. 사교적인 모임을 선호하나요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "9. 종종 사람들의 감정을 고려하나요?",
        "options": ["예", "아니오"]
    },
    {
        "question": "10. 부정확한 정보를 듣고 흥미를 느끼나요?",
        "options": ["예", "아니오"]
    }
]

# MBTI 계산 함수
def calculate_mbti(answers):
    e_score = answers.count("예")
    i_score = len(answers) - e_score

    if e_score > i_score:
        e_i = "E"  # 외향
    else:
        e_i = "I"  # 내향

    # 각 질문의 기준에 따라 1점씩 추가
    t_score = 0
    f_score = 0
    for idx, answer in enumerate(answers):
        if idx in [5, 6]:  # T/F 기준 질문
            if answer == "예":
                t_score += 1
            else:
                f_score += 1

    if t_score > f_score:
        t_f = "T"  # 사고
    else:
        t_f = "F"  # 감정

    j_score = 0
    p_score = 0
    for idx, answer in enumerate(answers):
        if idx in [1, 3, 7]:  # J/P 기준 질문
            if answer == "예":
                j_score += 1
            else:
                p_score += 1

    if j_score > p_score:
        j_p = "J"  # 판단
    else:
        j_p = "P"  # 인식

    return e_i + t_f + j_p

# Streamlit 애플리케이션 제목
st.title("MBTI 유형 검사")

# 답변을 저장할 리스트
answers = []

# 질문 출력
for question in questions:
    answer = st.selectbox(question["question"], question["options"], key=question["question"])
    answers.append(answer)

# 제출 버튼
if st.button("결과 확인"):
    mbti = calculate_mbti(answers)
    st.write(f"당신의 MBTI 유형은: **{mbti}**입니다.")


