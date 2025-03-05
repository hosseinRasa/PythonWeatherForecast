from flask import Flask, request, render_template
from weather import Weather
from waitress import serve

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    # city = request.args.get('city')
    # print(city)
    return  render_template('index.html')
@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city.strip():
        return index()
    city_weather = Weather(city)
    result = city_weather.get_weather()
    if result['cod'] != 200:
        return render_template('city_not_found.html')
    return render_template('weather.html', city = city, result_state = result)
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)




