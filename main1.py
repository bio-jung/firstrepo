# 간단한 MBTI 검사지 만들기 (Python)

def ask_questions():
    print("\n각 질문에 대해 a 또는 b로 답해주세요.\n")

    answers = []

    questions = [
        ("1. 사람들과 함께 있을 때 에너지가 생긴다.", "a", "혼자 있을 때 에너지가 충전된다.", "b"),
        ("2. 사실과 현실을 중시한다.", "a", "아이디어와 가능성을 중시한다.", "b"),
        ("3. 결정을 내릴 때 논리와 객관성을 우선시한다.", "a", "결정을 내릴 때 감정과 가치를 우선시한다.", "b"),
        ("4. 계획 세우는 것을 좋아한다.", "a", "상황에 따라 유연하게 대응하는 것을 좋아한다.", "b")
    ]

    for q in questions:
        print(q[0], "(a)")
        print(q[2], "(b)")
        while True:
            answer = input("a 또는 b를 입력하세요: ").lower()
            if answer in ["a", "b"]:
                answers.append(answer)
                break
            else:
                print("잘못 입력했습니다. 다시 입력해주세요.")

    return answers


def determine_mbti(answers):
    mbti = ""
    mbti += "E" if answers[0] == "a" else "I"
    mbti += "S" if answers[1] == "a" else "N"
    mbti += "T" if answers[2] == "a" else "F"
    mbti += "J" if answers[3] == "a" else "P"
    return mbti


def main():
    print("간단한 MBTI 테스트에 오신 것을 환영합니다!")
    answers = ask_questions()
    result = determine_mbti(answers)
    print(f"\n당신의 MBTI 유형은 {result}입니다!")


if __name__ == "__main__":
    main()
