import os
import requests

# 저장할 폴더 생성
download_folder = "flags"
os.makedirs(download_folder, exist_ok=True)

# 다운로드할 ISO2 국가 코드 리스트 (예시로 일부만)
country_codes = [
    'kr', 'us', 'jp', 'cn', 'fr', 'de', 'br', 'gb', 'ru', 'it', 'es', 'in', 'ca', 'au'
]

# Base URL
base_url = "https://flagcdn.com/w320/"

# 각 국가 코드에 대해 다운로드
for code in country_codes:
    url = f"{base_url}{code}.png"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = os.path.join(download_folder, f"{code}.png")
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {code}.png")
    else:
        print(f"Failed to download: {code}.png (Status Code: {response.status_code})")
