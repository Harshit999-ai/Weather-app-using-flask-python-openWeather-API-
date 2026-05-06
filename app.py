#This is simple code for running our app live using flask
from flask import Flask,render_template,request
from weather_fetcher import get_weather

weather_api = "e5ee67b7cc420de7a779275e0ac8895e"

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def home():
    weather = None
    error = None
    if request.method == 'POST':
        city = request.form["city"]
        weather = get_weather(city,weather_api)
        return render_template("index.html",weather=weather,error=error)
    else:
        return "error"
if __name__ == "__main__":
    app.run(debug = True,port = 5000)
