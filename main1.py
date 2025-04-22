# Streamlit을 활용한 MBTI 검사 앱

import streamlit as st

def main():
    st.title("🌟 간단한 MBTI 성격 유형 테스트")
    st.write("아래 질문에 답하고 나의 MBTI를 알아보세요!")

    with st.form("mbti_form"):
        st.subheader("1. 에너지 방향")
        q1 = st.radio(
            "사람들과 함께 있을 때 에너지가 생긴다?",
            ("예", "아니오")
        )

        st.subheader("2. 인식 방식")
        q2 = st.radio(
            "사실과 현실을 중시하는 편이다?",
            ("예", "아니오")
        )

        st.subheader("3. 판단 기준")
        q3 = st.radio(
            "결정을 내릴 때 논리와 객관성을 우선시한다?",
            ("예", "아니오")
        )

        st.subheader("4. 생활 양식")
        q4 = st.radio(
            "계획 세우는 것을 좋아한다?",
            ("예", "아니오")
        )

        submitted = st.form_submit_button("MBTI 결과 보기")

    if submitted:
        mbti = ""
        mbti += "E" if q1 == "예" else "I"
        mbti += "S" if q2 == "예" else "N"
        mbti += "T" if q3 == "예" else "F"
        mbti += "J" if q4 == "예" else "P"

        st.success(f"🎉 당신의 MBTI 유형은 **{mbti}** 입니다!")

        # MBTI별 간단한 설명 제공
        mbti_descriptions = {
            "INTJ": "전략가형 - 독립적이며 목표 지향적.",
            "INTP": "논리형 - 탐구적이고 호기심 많은 성격.",
            "ENTJ": "지도자형 - 대담하고 결단력 있는 성격.",
            "ENTP": "변론가형 - 혁신적이고 도전적인 성격.",
            "INFJ": "옹호자형 - 깊이 있는 통찰력과 감성을 지님.",
            "INFP": "중재자형 - 이상주의적이고 충성심 있는 성격.",
            "ENFJ": "선도자형 - 사교적이고 타인을 이끄는 성격.",
            "ENFP": "활동가형 - 열정적이고 창의적인 성격.",
            "ISTJ": "현실주의자형 - 신뢰할 수 있고 조직적인 성격.",
            "ISFJ": "수호자형 - 헌신적이고 따뜻한 성격.",
            "ESTJ": "경영자형 - 체계적이고 리더십 강한 성격.",
            "ESFJ": "집정관형 - 친절하고 협력적인 성격.",
            "ISTP": "장인형 - 실용적이며 유연한 성격.",
            "ISFP": "모험가형 - 감성적이고 자유로운 성격.",
            "ESTP": "사업가형 - 에너지 넘치고 현실적인 성격.",
            "ESFP": "연예인형 - 사교적이고 즉흥적인 성격."
        }

        st.info(mbti_descriptions.get(mbti, "설명 준비 중입니다."))

if __name__ == "__main__":
    main()
