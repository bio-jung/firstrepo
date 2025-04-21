import matplotlib.pyplot as plt

# 연도와 평균기온 데이터 (추정치 기반 예시)
years = list(range(1980, 2025))
# 간단한 예시: 1980년 11.5℃에서 시작해서, 점진적으로 13.5℃까지 증가한다고 가정
temperatures = [
    11.5 + (13.5 - 11.5) / (2024 - 1980) * (year - 1980) for year in years
]

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(years, temperatures, marker='o', linestyle='-', linewidth=2)
plt.title('1980~2024년 서울특별시 연평균 기온 변화 (예시)', fontsize=18)
plt.xlabel('연도', fontsize=14)
plt.ylabel('연평균 기온 (℃)', fontsize=14)
plt.grid(True)
plt.xticks(range(1980, 2025, 5), rotation=45)
plt.tight_layout()

# 그래프 보여주기
plt.show()

