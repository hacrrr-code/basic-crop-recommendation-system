from flask import Flask, render_template, request

app = Flask(__name__)


def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    """
    Very basic rule-based crop recommendation.
    Replace this with a trained ML model later for real predictions.
    """
    if ph < 5.5:
        return "Tea"
    elif rainfall > 200 and temperature > 25:
        return "Rice"
    elif temperature < 20 and rainfall < 100:
        return "Wheat"
    elif N > 80 and P > 40 and K > 40:
        return "Sugarcane"
    elif humidity > 70 and temperature > 20:
        return "Maize"
    else:
        return "Millets"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temperature = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        result = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)
    except (KeyError, ValueError):
        result = "Invalid input, please check your values."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
