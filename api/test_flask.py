from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FORTUNES = {
    "aries": {"today": "白羊座今天运势大好，适合大胆行动！", "tomorrow": "明日宜静不宜动，保持低调。"},
    "taurus": {"today": "金牛座财运亨通，小有收获。", "tomorrow": "注意健康，避免过度劳累。"},
    "gemini": {"today": "双子座创意迸发，适合学习新事物。", "tomorrow": "人际关系顺畅，贵人相助。"},
    "cancer": {"today": "巨蟹座家庭和睦，心情舒畅。", "tomorrow": "感情升温，适合表达心意。"},
    "leo": {"today": "狮子座魅力四射，容易吸引关注。", "tomorrow": "工作顺利，领导认可。"},
    "virgo": {"today": "处女座效率极高，事半功倍。", "tomorrow": "注意细节，避免小错。"},
    "libra": {"today": "天秤座人缘极佳，适合社交。", "tomorrow": "决策果断，抓住机会。"},
    "scorpio": {"today": "天蝎座直觉敏锐，洞察力强。", "tomorrow": "财运上升，投资有回报。"},
    "sagittarius": {"today": "射手座活力充沛，适合运动。", "tomorrow": "旅行运佳，放松心情。"},
    "capricorn": {"today": "摩羯座事业稳步上升，收获认可。", "tomorrow": "坚持到底，成功在望。"},
    "aquarius": {"today": "水瓶座灵感爆发，创意无限。", "tomorrow": "团队合作，成果显著。"},
    "pisces": {"today": "双鱼座梦境成真，幸福感满满。", "tomorrow": "艺术灵感迸发，创作顺利。"}
}

@app.route('/api/fortune/daily/<sign>/<day>')
def get_fortune(sign, day):
    fortune = FORTUNES.get(sign.lower(), {}).get(day.lower(), "暂无此星座运势")
    return jsonify({"sign": sign, "day": day, "fortune": fortune})

@app.route('/')
def home():
    return jsonify({"message": "Fortune Handchain API is running!"})

if __name__ == '__main__':
    app.run(debug=True)
