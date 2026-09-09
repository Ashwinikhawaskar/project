from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Python Addition App!"

@app.route("/add")
def addition():
    num1 = int(request.args.get("num1", 0))
    num2 = int(request.args.get("num2", 0))

    result = num1 + num2

    return f"Addition of {num1} + {num2} = {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)