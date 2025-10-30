from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FORTUNES = {
    "aries": {"today": "白羊座今天运势大好，适合大胆行动！"},
    "taurus": {"today": "金牛座财运旺盛。"},
    "gemini": {"today": "双子座创意迸发，适合学习新事物。"}
}

@app.route('/api/fortune/daily/<sign>/<day>')
def get_fortune(sign, day):
    fortune = FORTUNES.get(sign.lower(), {}).get(day.lower(), "暂无运势")
    return jsonify({"sign": sign, "day": day, "fortune": fortune})

@app.route('/')
def home():
    return jsonify({"message": "Fortune API is running!"})

# ===== Vercel 必须的适配器 =====
try:
    from vercel_python_wsgi import wsgi_app
    wsgi_app = wsgi_app(app)
except ImportError:
    # 本地运行时忽略
    pass
