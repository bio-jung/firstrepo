#!/usr/bin/env python3
"""
MBTI Quiz (Korean Version)
--------------------------
이 스크립트는 간단한 12개의 질문을 통해 사용자의 MBTI 유형을 추정합니다.
각 질문은 두 선택지(A/B)로 구성되어 있으며, 네 가지 차원(E/I, S/N, T/F, J/P)에 대응합니다.
사용자가 입력을 잘못했을 경우 다시 입력하도록 안내해 안전하게 실행됩니다.

사용 방법:
$ python mbti_quiz.py

결과가 4차원 중 하나에서 동점인 경우, 해당 차원은 '-' 로 표시됩니다.
"""

import sys

QUESTIONS = [
    {
        "text": "1. 사교 모임에서 당신은 (A) 모르는 사람과도 적극적으로 교류한다 (B) 익숙한 사람과 주로 교류한다",
        "dimension": "EI",
        "a": "E",
        "b": "I",
    },
    {
        "text": "2. 새로운 정보를 배울 때 (A) 구체적 사실과 실용적 예시를 선호한다 (B) 추상적 이론과 가능성을 선호한다",
        "dimension": "SN",
        "a": "S",
        "b": "N",
    },
    {
        "text": "3. 의사결정 시 (A) 논리적 일관성을 중시한다 (B) 개인적 가치와 조화를 중시한다",
        "dimension": "TF",
        "a": "T",
        "b": "F",
    },
    {
        "text": "4. 작업 방식을 선택한다면 (A) 계획적이고 조직적인 방식을 선호한다 (B) 자율적이고 유연한 방식을 선호한다",
        "dimension": "JP",
        "a": "J",
        "b": "P",
    },
    {
        "text": "5. 에너지를 충전할 때 (A) 외부 활동에 참여하며 충전한다 (B) 혼자 시간을 보내며 충전한다",
        "dimension": "EI",
        "a": "E",
        "b": "I",
    },
    {
        "text": "6. 설명할 때 (A) 구체적 세부사항을 중심으로 설명한다 (B) 전체적인 그림과 비유를 활용해 설명한다",
        "dimension": "SN",
        "a": "S",
        "b": "N",
    },
    {
        "text": "7. 문제 해결 시 (A) 객관적 데이터와 분석을 신뢰한다 (B) 직관과 감정을 신뢰한다",
        "dimension": "TF",
        "a": "T",
        "b": "F",
    },
    {
        "text": "8. 결정을 내릴 때 (A) 빠르게 결정하고 확정 짓는다 (B) 가능한 한 옵션을 열어 둔다",
        "dimension": "JP",
        "a": "J",
        "b": "P",
    },
    {
        "text": "9. 대화 중 (A) 즉시 자신의 생각을 말한다 (B) 먼저 듣고 난 뒤 말한다",
        "dimension": "EI",
        "a": "E",
        "b": "I",
    },
    {
        "text": "10. 문제 해결 접근 시 (A) 현재 현실을 우선 고려한다 (B) 미래 가능성을 우선 고려한다",
        "dimension": "SN",
        "a": "S",
        "b": "N",
    },
    {
        "text": "11. 스트레스 상황에서 (A) 분석과 논리를 우선한다 (B) 사람들의 감정을 우선한다",
        "dimension": "TF",
        "a": "T",
        "b": "F",
    },
    {
        "text": "12. 하루 일정을 (A) 일정표나 할 일 목록으로 관리한다 (B) 상황에 따라 유동적으로 대응한다",
        "dimension": "JP",
        "a": "J",
        "b": "P",
    },
]

DIMENSIONS = [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]


def ask_questions():
    """질문을 순회하며 점수를 계산한다."""
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    for q in QUESTIONS:
        while True:
            print(q["text"])
            choice = input("  ▶ A/B 중 선택: ").strip().upper()
            if choice in {"A", "B"}:
                selected = q["a"] if choice == "A" else q["b"]
                scores[selected] += 1
                print()
                break
            else:
                print("  잘못된 입력입니다. 'A' 또는 'B'를 입력해 주세요.\n")
    return scores


def determine_mbti(scores):
    """점수에 따라 MBTI 유형을 결정한다."""
    result = ""
    for first, second in DIMENSIONS:
        if scores[first] > scores[second]:
            result += first
        elif scores[second] > scores[first]:
            result += second
        else:
            result += "-"  # 동점인 경우
    return result


def main():
    print("\n================ MBTI 간이 테스트 ================\n")
    scores = ask_questions()
    mbti_type = determine_mbti(scores)

    print("================  결과  ================\n")
    if "-" in mbti_type:
        print(
            f"일부 차원에서 동점이 발생했습니다. 잠정적인 MBTI 유형: {mbti_type}\n"
            "'-' 로 표시된 차원은 추가 질문이나 자신에 대한 더 깊은 고찰을 통해 결정해 보세요."
        )
    else:
        print(f"당신의 MBTI 유형은: {mbti_type}")

    print("\n==============================================\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\n테스트가 중단되었습니다. 안녕히 가세요!")
