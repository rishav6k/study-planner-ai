from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({
        "message": "Environment reset successful"
    })

@app.route("/run", methods=["POST"])
def run():
    data = request.json

    energy = data.get("energy", 50)
    time = data.get("time", 60)

    subjects = ["maths", "science", "english", "history"]
    plan = []

    for i in range(4):
        subject = random.choice(subjects)
        plan.append(subject)

    return jsonify({
        "plan": plan,
        "energy": energy,
        "time": time,
        "message": "Plan generated"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
