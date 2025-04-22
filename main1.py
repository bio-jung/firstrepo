import streamlit as st
import pandas as pd

# 데이터: 나라, 수도, 국기 URL
data = {
    "국가": [
        "대한민국", "미국", "일본", "중국", "영국",
        "프랑스", "독일", "이탈리아", "스페인", "캐나다",
        "호주", "브라질", "인도", "멕시코", "러시아",
        "사우디아라비아", "네덜란드", "스웨덴", "노르웨이", "핀란드"
    ],
    "수도": [
        "서울", "워싱턴 D.C.", "도쿄", "베이징", "런던",
        "파리", "베를린", "로마", "마드리드", "오타와",
        "캔버라", "브라질리아", "뉴델리", "멕시코시티", "모스크바",
        "리야드", "암스테르담", "스톡홀름", "오슬로", "헬싱키"
    ],
    "국기 URL": [
        "https://upload.wikimedia.org/wikipedia/commons/0/09/Flag_of_South_Korea.svg",
        "https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg",
        "https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg",
        "https://upload.wikimedia.org/wikipedia/commons/0/0d/Flag_of_China.svg",
        "https://upload.wikimedia.org/wikipedia/en/b/be/Flag_of_the_United_Kingdom.svg",
        "https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg",
        "https://upload.wikimedia.org/wikipedia/en/b/ba/Flag_of_Germany.svg",
        "https://upload.wikimedia.org/wikipedia/commons/0/03/Flag_of_Italy.svg",
        "https://upload.wikimedia.org/wikipedia/en/9/9a/Flag_of_Spain.svg",
        "https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Canada.svg",
        "https://upload.wikimedia.org/wikipedia/commons/b/b9/Flag_of_Australia.svg",
        "https://upload.wikimedia.org/wikipedia/en/0/05/Flag_of_Brazil.svg",
        "https://upload.wikimedia.org/wikipedia/en/9/9c/Flag_of_India.svg",
        "https://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Mexico.svg",
        "https://upload.wikimedia.org/wikipedia/en/f/f3/Flag_of_Russia.svg",
        "https://upload.wikimedia.org/wikipedia/commons/4/43/Flag_of_Saudi_Arabia.svg",
        "https://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg",
        "https://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Sweden.svg",
        "https://upload.wikimedia.org/wikipedia/commons/e/e0/Flag_of_Norway.svg",
        "https://upload.wikimedia.org/wikipedia/commons/b/b0/Flag_of_Finland.svg"
    ]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

st.title("🌍 세계 20개국의 수도와 국기")

# 국기 이미지를 실제로 표시할 컬럼 추가
def get_flag_image(url):
    return f"![Flag]({url})"

df["국기"] = df["국기 URL"].apply(get_flag_image)

# 필요없는 URL 컬럼 제거
df_display = df.drop(columns=["국기 URL"])

# Streamlit에 마크다운 테이블 형태로 출력
st.markdown(
    df_display.to_markdown(index=False),
    unsafe_allow_html=True
)

st.caption("※ 이미지는 Streamlit 기본 테이블에 직접 삽입할 수 없기 때문에 마크다운을 이용해 표현했습니다.")
