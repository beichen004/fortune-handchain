from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FORTUNES = {
    "aries": {"today": "白羊座今天运势大好，适合大胆行动！"},
    "taurus": {"today": "金牛座财运旺盛。"},
    "gemini": {"today": "双子座创意迸发，适合学习新事物。"},
    "cancer": {"today": "巨蟹座家庭和睦，心情舒畅。"},
    "leo": {"today": "狮子座魅力四射，容易吸引关注。"},
    "virgo": {"today": "处女座效率极高，事半功倍。"},
    "libra": {"today": "天秤座人缘极佳，适合社交。"},
    "scorpio": {"today": "天蝎座直觉敏锐，洞察力强。"},
    "sagittarius": {"today": "射手座活力充沛，适合运动。"},
    "capricorn": {"today": "摩羯座事业稳步上升，收获认可。"},
    "aquarius": {"today": "水瓶座灵感爆发，创意无限。"},
    "pisces": {"today": "双鱼座梦境成真，幸福感满满。"}
}

@app.route('/api/fortune/daily/<sign>/<day>')
def get_fortune(sign, day):
    fortune = FORTUNES.get(sign.lower(), {}).get(day.lower(), "暂无此星座运势")
    return jsonify({"sign": sign, "day": day, "fortune": fortune})

@app.route('/')
def home():
    return jsonify({"message": "Fortune API is running!"})

if __name__ == '__main__':
    app.run(debug=True)
