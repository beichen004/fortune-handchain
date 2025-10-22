import requests
from bs4 import BeautifulSoup

def get_horoscope_by_day(zodiac_sign: int, day: str):
    if day.lower() == 'today':
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day.lower()}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text if data else "运势数据暂不可用"

