from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/weather/<city>")
def weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url, timeout=10).json()

    current = data["current_condition"][0]

    return jsonify({
        "temperature_c": current.get("temp_C"),
        "humidity": current.get("humidity"),
        "wind_kmph": current.get("windspeedKmph"),
        "description": current["weatherDesc"][0]["value"],
        "wind_dir": current.get("winddir16Point"),
        "visibility_km": current.get("visibility"),
        "feelslike": current.get("FeelsLikeC")
    })

if __name__ == "__main__":
    app.run(debug=True)
