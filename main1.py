import matplotlib.pyplot as plt

# 데이터
years = [2000, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025]
audience = [120, 135, 160, 155, 110, 90, 100, 120, 140, 150]

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(years, audience)
plt.title('2000~2025년 클래식 음악 관람객 변화 (바 차트)', fontsize=16)
plt.xlabel('연도', fontsize=14)
plt.ylabel('관람객 수 (만 명)', fontsize=14)
plt.grid(axis='y')  # y축에만 그리드 표시
plt.xticks(years, rotation=45)
plt.tight_layout()

# 그래프 보여주기
plt.show()

