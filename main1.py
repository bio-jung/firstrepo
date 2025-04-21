import pandas as pd

data = {
    '국가': ['대한민국', '미국', '일본', '중국', '독일', '프랑스', '영국', '인도', '호주', '브라질'],
    '국기 이미지 URL': [
        'https://flagcdn.com/w320/kr.png',
        'https://flagcdn.com/w320/us.png',
        'https://flagcdn.com/w320/jp.png',
        'https://flagcdn.com/w320/cn.png',
        'https://flagcdn.com/w320/de.png',
        'https://flagcdn.com/w320/fr.png',
        'https://flagcdn.com/w320/gb.png',
        'https://flagcdn.com/w320/in.png',
        'https://flagcdn.com/w320/au.png',
        'https://flagcdn.com/w320/br.png'
    ],
    '수도': ['서울', '워싱턴 D.C.', '도쿄', '베이징', '베를린', '파리', '런던', '뉴델리', '캔버라', '브라질리아'],
    '인구수': ['5,100만', '3억 3,100만', '1억 2,500만', '14억 2,000만', '8,300만', '6,700만', '6,700만', '14억 1,000만', '2,600만', '2억 1,400만']
}

df = pd.DataFrame(data)

# HTML로 변환 (Jupyter Notebook에서 이미지 표시 가능)
from IPython.display import HTML

def path_to_image_html(path):
    return f'<img src="{path}" width="60" >'

HTML(df.to_html(escape=False, formatters={'국기 이미지 URL': path_to_image_html}))
