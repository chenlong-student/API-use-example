from flask import Flask, request, jsonify
from pyngrok import ngrok

app = Flask(__name__)


@app.route("/compute", methods=["POST"])
def compute():
    """计算 num = sum(b + i*a) for i in 1..n"""
    data = request.get_json(silent=True) or {}
    a = data["a"]
    b = data["b"]
    n = data["n"]

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
    # 打开公网隧道，生成一个公网 URL
    public_url = ngrok.connect(5001)
    print(f"公网地址: {public_url}")
    print("其他设备（不同 WiFi）可通过此地址调用接口")
    # 启动 Flask，host=0.0.0.0 允许所有 IP 访问
    app.run(host="0.0.0.0", port=5001)
