from flask import jsonify
from core import app
from core.utils import get_horoscope_by_day
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest
from googletrans import Translator

ZODIAC_SIGNS = {
    "aries": 1, "taurus": 2, "gemini": 3, "cancer": 4, "leo": 5, "virgo": 6,
    "libra": 7, "scorpio": 8, "sagittarius": 9, "capricorn": 10, "aquarius": 11, 
"pisces": 12
}

translator = Translator()

@app.route('/api/fortune/daily/<sign>/<day>')
def daily_horoscope(sign, day):
    try:
        zodiac_num = ZODIAC_SIGNS[sign.lower()]
        if day != 'today':
            datetime.strptime(day, '%Y-%m-%d')
        horoscope_data = get_horoscope_by_day(zodiac_num, day)
        translated_fortune = translator.translate(horoscope_data, 
dest='zh-cn').text
        return jsonify({"success": True, "sign": sign.capitalize(), "day": day, 
"fortune": translated_fortune})
    except KeyError:
        raise NotFound('无效的星座')
    except ValueError:
        raise BadRequest('日期格式错误，应为YYYY-MM-DD或today')

