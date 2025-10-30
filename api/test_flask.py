from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FORTUNES = {
    "aries": {"today": "白羊座今天运势大好！", "tomorrow": "明日宜静不宜动"},
    "taurus": {"today": "金牛座财运亨通！", "tomorrow": "注意健康"}
}

@app.route('/api/fortune/daily/<sign>/<day>')
def get_fortune(sign, day):
    fortune = FORTUNES.get(sign.lower(), {}).get(day.lower(), "暂无运势")
    return jsonify({
        "sign": sign,
        "day": day,
        "fortune": fortune
    })

if __name__ == '__main__':
    app.run(debug=True)
