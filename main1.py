import streamlit as st

# 질문과 MBTI 차원 연결
questions = [
    {"question": "1. 당신은 사람들 사이에서 에너지를 얻는 편인가요?", "dimension": "EI"},
    {"question": "2. 계획을 세우는 것을 좋아하나요?", "dimension": "JP"},
    {"question": "3. 새로운 아이디어를 생각하는 것이 흥미로운가요?", "dimension": "SN"},
    {"question": "4. 타인을 돕는 것을 좋아하나요?", "dimension": "TF"},
    {"question": "5. 즉흥적인 결정을 잘 내리나요?", "dimension": "JP"},
    {"question": "6. 감정보다 논리를 더 중시하나요?", "dimension": "TF"},
    {"question": "7. 상황에 따라 변화를 좋아하나요?", "dimension": "JP"},
    {"question": "8. 사교적인 모임을 선호하나요?", "dimension": "EI"},
    {"question": "9. 종종 사람들의 감정을 고려하나요?", "dimension": "TF"},
    {"question": "10. 부정확한 정보를 듣고 흥미를 느끼나요?", "dimension": "SN"},
]

# MBTI 계산 함수
def calculate_mbti(responses):
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for idx, answer in enumerate(responses):
        dimension = questions[idx]["dimension"]
        if dimension == "EI":
            if answer == "예":
                scores["E"] += 1
            else:
                scores["I"] += 1
        elif dimension == "SN":
            if answer == "예":
                scores["N"] += 1
            else:
                scores["S"] += 1
        elif dimension == "TF":
            if answer == "예":
                scores["T"] += 1
            else:
                scores["F"] += 1
        elif dimension == "JP":
            if answer == "예":
                scores["J"] += 1
            else:
                scores["P"] += 1

    result = ""
    result += "E" if scores["E"] >= scores["I"] else "I"
    result += "S" if scores["S"] >= scores["N"] else "N"
    result += "T" if scores["T"] >= scores["F"] else "F"
    result += "J" if scores["J"] >= scores["P"] else "P"
    return result

# Streamlit 인터페이스
st.title("🔍 MBTI 간단 검사")

answers = []

st.write("아래 질문에 답변해 주세요:")

for idx, q in enumerate(questions):
    answer = st.selectbox(q["question"], ["예", "아니오"], key=idx)
    answers.append(answer)

if st.button("결과 확인"):
    mbti_type = calculate_mbti(answers)
    st.success(f"당신의 MBTI 유형은 **{mbti_type}** 입니다!")


