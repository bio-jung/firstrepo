def mbti_test():
    print("MBTI 테스트에 오신 것을 환영합니다! 각 질문에 대해 A 또는 B를 입력하세요.")

    def get_answer():
        while True:
            answer = input("답변 (A/B): ").strip().upper()
            if answer in ['A', 'B']:
                return answer
            else:
                print("잘못된 입력입니다. A 또는 B만 입력해주세요.")

    ei_score, sn_score, tf_score, jp_score = 0, 0, 0, 0

    # E/I 질문
    print("1. 사람들과 함께 있을 때 에너지가 충전된다 (A) / 혼자 있을 때 에너지가 충전된다 (B)")
    ei_score += 1 if get_answer() == 'A' else -1

    print("2. 처음 만난 사람과 쉽게 대화를 시작할 수 있다 (A) / 먼저 말을 걸기가 어렵다 (B)")
    ei_score += 1 if get_answer() == 'A' else -1

    print("9. 파티나 모임에서 에너지를 얻는다 (A) / 소규모 만남이나 조용한 시간을 선호한다 (B)")
    ei_score += 1 if get_answer() == 'A' else -1

    # S/N 질문
    print("3. 현재에 집중하고 구체적인 사실을 중시한다 (A) / 미래의 가능성과 아이디어를 상상한다 (B)")
    sn_score += 1 if get_answer() == 'A' else -1

    print("4. 경험을 중시하고 실질적인 것을 선호한다 (A) / 직관과 영감을 중시한다 (B)")
    sn_score += 1 if get_answer() == 'A' else -1

    print("10. 실용적인 조언을 선호한다 (A) / 창의적이고 영감을 주는 조언을 선호한다 (B)")
    sn_score += 1 if get_answer() == 'A' else -1

    # T/F 질문
    print("5. 논리적 분석을 통해 결정을 내린다 (A) / 사람들의 감정을 고려해 결정을 내린다 (B)")
    tf_score += 1 if get_answer() == 'A' else -1

    print("6. 문제 해결 시 객관적 원칙을 따르는 편이다 (A) / 상황에 따라 융통성 있게 판단하는 편이다 (B)")
    tf_score += 1 if get_answer() == 'A' else -1

    # J/P 질문
    print("7. 계획을 세우고 미리 준비하는 것을 좋아한다 (A) / 즉흥적으로 결정하는 것을 좋아한다 (B)")
    jp_score += 1 if get_answer() == 'A' else -1

    print("8. 하루 일정을 체계적으로 관리하는 것을 선호한다 (A) / 자유롭게 그날그날 다르게 행동하는 것을 선호한다 (B)")
    jp_score += 1 if get_answer() == 'A' else -1

    # 최종 결과
    mbti = ''
    mbti += 'E' if ei_score > 0 else 'I'
    mbti += 'S' if sn_score > 0 else 'N'
    mbti += 'T' if tf_score > 0 else 'F'
    mbti += 'J' if jp_score > 0 else 'P'

    print(f\"\\n당신의 MBTI 유형은 {mbti}입니다!\")

if __name__ == \"__main__\":
    mbti_test()
