from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/compute", methods=["POST"])
def compute():
    """计算 num = sum(b + i*a) for i in 1..n"""
    data = request.get_json(silent=True) or {}
    a = data.get("a", 10)
    b = data.get("b", 1)
    n = data.get("n", 9)

    # 类型校验
    try:
        a = int(a)
        b = int(b)
        n = int(n)
    except (ValueError, TypeError):
        return jsonify({"error": "a、b、n 必须是整数"}), 400

    num = 0
    for i in range(1, n + 1):
        num = num + (b + i * a)

    return jsonify({"result": num})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
