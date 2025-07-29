from flask import Flask, render_template, request
from utils.prediction_model import predict_food_waste
from utils.weather import get_weather

app = Flask(__name__, template_folder='templates10', static_folder='static10')

@app.route('/')
def index():
    return render_template('index10.html')

@app.route('/predict', methods=['POST'])
def predict():
    city = request.form['city']
    menu_item = request.form['menu_item']
    people_count = int(request.form['people_count'])

    weather = get_weather(city)

    if 'error' in weather:
        return render_template('results10.html', error=weather['error'])

    result = predict_food_waste(menu_item, weather, people_count)

    if isinstance(result, str):  # Error case
        return render_template('results10.html', error=result)

    return render_template(
        'results10.html',
        prediction=result["required"],
        waste=result["waste"],
        weather=weather,
        city=city,
        menu_item=menu_item
    )

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5010)
