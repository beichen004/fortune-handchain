from flask import Flask, jsonify
from flask_cors import CORS   # <-- 新增

app = Flask(__name__)
CORS(app)                     # <-- 允许所有来源跨域

# 示例运势数据（可替换为你的真实数据）
FORTUNES = {
    "aries": {
        "today": "白羊座今天运势大好，适合大胆行动！",
        "tomorrow": "明日宜静不宜动，保持低调。"
    },
    "taurus": {
        "today": "金牛座财运亨通，小有收获。",
        "tomorrow": "注意健康，避免过度劳累。"
    }
    # 可继续添加其他星座...
}

@app.route('/api/fortune/daily/<sign>/<day>')
def get_fortune(sign, day):
    fortune = FORTUNES.get(sign.lower(), {}).get(day.lower(), "暂无运势")
    return jsonify({
        "sign": sign,
        "day": day,
        "fortune": fortune
    })

# 可选：根路径返回 hello，方便测试
@app.route('/')
def home():
    return jsonify({"message": "Fortune API is running!"})

if __name__ == '__main__':
    app.run(debug=True)
