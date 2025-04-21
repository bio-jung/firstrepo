import matplotlib.pyplot as plt

# 데이터
years = [2000, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025]
audience = [120, 135, 160, 155, 110, 90, 100, 120, 140, 150]

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(years, audience, marker='o', linestyle='-', linewidth=2)
plt.title('2000~2025년 클래식 음악 관람객 변화', fontsize=16)
plt.xlabel('연도', fontsize=14)
plt.ylabel('관람객 수 (만 명)', fontsize=14)
plt.grid(True)
plt.xticks(years, rotation=45)
plt.tight_layout()

# 그래프 보여주기
plt.show()

st.title("나의 첫 번째 스트림릿 사이트")
st.write("안녕하세요~ 배미정입니다^^")
