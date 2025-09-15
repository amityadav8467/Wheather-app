from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "76ed0ccde9f9c9583b48db420f5fd6a3"  # replace with your OpenWeatherMap API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=76ed0ccde9f9c9583b48db420f5fd6a3&units=metric"
            response = requests.get(url).json()

            if response.get("cod") != "404":
                weather_data = {
                    "city": city.title(),
                    "temperature": response["main"]["temp"],
                    "humidity": response["main"]["humidity"],
                    "wind": response["wind"]["speed"],
                    "description": response["weather"][0]["description"].title(),
                }
            else:
                weather_data = {"error": "City not found. Please try again."}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
