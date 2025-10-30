from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FORTUNES = {
    "aries": {
        "today": "白羊座今天运势大好，适合大胆行动！",
        "tomorrow": "明日宜静不宜动。"
    },
    "taurus": {
        "today": "金牛座财运旺盛。",
        "tomorrow": "注意健康。"
    }
}

@app.route('/api/fortune/daily/<sign>/<day>')
def get_fortune(sign, day):
    fortune = FORTUNES.get(sign.lower(), {}).get(day.lower(), "暂无运势")
    return jsonify({
        "sign": sign,
        "day": day,
        "fortune": fortune
    })

@app.route('/')
def home():
    return jsonify({"message": "Fortune API is running!"})

# Vercel 必须的 handler
def handler(event, context):
    from serverless_wsgi import handle_request
    return handle_request(app, event, context)
