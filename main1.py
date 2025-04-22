# Streamlit을 활용한 MBTI 검사 앱 (10문항, 명확한 선택지 버전)

import streamlit as st

def main():
    st.title("🌟 심층 MBTI 성격 유형 테스트")
    st.write("10개의 질문에 답하고 더 정밀한 나의 MBTI를 알아보세요!")

    with st.form("mbti_form"):
        st.subheader("에너지 방향 (E vs I)")
        q1 = st.radio("1. 사람들과 함께 있을 때 에너지가 생긴다?", ("예: 에너지가 생긴다", "아니오: 혼자 있을 때 충전된다"))
        q2 = st.radio("2. 사람들과 대화하는 것이 즐겁다?", ("예: 즐겁다", "아니오: 피곤하다"))

        st.subheader("인식 방식 (S vs N)")
        q3 = st.radio("3. 사실과 현재에 집중하는 편이다?", ("예: 사실과 현재", "아니오: 가능성과 미래"))
        q4 = st.radio("4. 추상적 개념이나 미래 가능성에 관심이 많다?", ("예: 관심 있다", "아니오: 별로 관심 없다"))

        st.subheader("판단 기준 (T vs F)")
        q5 = st.radio("5. 논리적 분석을 통해 결정을 내린다?", ("예: 논리적 분석", "아니오: 감정과 가치"))
        q6 = st.radio("6. 다른 사람의 감정을 고려해 결정을 내린다?", ("예: 감정 고려", "아니오: 논리 우선"))

        st.subheader("생활 양식 (J vs P)")
        q7 = st.radio("7. 계획 세우는 것을 선호한다?", ("예: 계획 선호", "아니오: 즉흥성 선호"))
        q8 = st.radio("8. 즉흥적인 결정을 선호한다?", ("예: 즉흥적 결정 선호", "아니오: 계획적 선호"))

        st.subheader("추가 심화 질문")
        q9 = st.radio("9. 대화 중 침묵이 불편하지 않다?", ("예: 불편하지 않다", "아니오: 불편하다"))
        q10 = st.radio("10. 일상의 작은 세부사항보다 큰 그림을 중요하게 생각한다?", ("예: 큰 그림 중시", "아니오: 세부사항 중시"))

        submitted = st.form_submit_button("MBTI 결과 보기")

    if submitted:
        # 각 지표별 점수 계산
        e_score = 0
        i_score = 0
        s_score = 0
        n_score = 0
        t_score = 0
        f_score = 0
        j_score = 0
        p_score = 0

        # 점수 배정
        e_score += 1 if q1.startswith("예") else 0
        e_score += 1 if q2.startswith("예") else 0
        i_score += 1 if q1.startswith("아니오") else 0
        i_score += 1 if q2.startswith("아니오") else 0

        s_score += 1 if q3.startswith("예") else 0
        s_score += 1 if q9.startswith("예") else 0
        n_score += 1 if q4.startswith("예") else 0
        n_score += 1 if q10.startswith("예") else 0

        t_score += 1 if q5.startswith("예") else 0
        f_score += 1 if q6.startswith("예") else 0

        j_score += 1 if q7.startswith("예") else 0
        p_score += 1 if q8.startswith("예") else 0

        # 결과 조합
        mbti = ""
        mbti += "E" if e_score >= i_score else "I"
        mbti += "S" if s_score >= n_score else "N"
        mbti += "T" if t_score >= f_score else "F"
        mbti += "J" if j_score >= p_score else "P"

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
