from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/fortune/daily/<sign>/<day>')
def get_fortune(sign, day):
    fortunes = {"aries": {"today": "A great day awaits!", "tomorrow": "Be cautious."}}
    fortune = fortunes.get(sign, {}).get(day, "No fortune available.")
    return jsonify({"fortune": fortune, "sign": sign, "day": day})

if __name__ == "__main__":
    app.run()
