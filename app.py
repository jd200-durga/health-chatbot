from flask import Flask, request, jsonify,render_template
from ai_engine.chatbot import get_response
import requests
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/alert")
def alert():

    alert_message = get_disease_alert()

    return alert_message

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    response = get_response(user_message)

    return jsonify({"reply": response})


@app.route("/whatsapp", methods=["POST"])
def whatsapp():

    incoming_message = request.values.get('Body')

    response = get_response(incoming_message)

    return response

def get_disease_alert():

    url = "https://disease.sh/v3/covid-19/all"

    data = requests.get(url).json()

    cases = data["cases"]

    return f"Current global COVID cases: {cases}"
if __name__ == "__main__":
    app.run(debug=True)