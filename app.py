from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import numpy as np
import os
import logging
app = Flask(__name__)
app.secret_key = 'flood-prediction-secret-key-2024'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
FEATURE_NAMES = ['Temp', 'Humidity', 'Cloud Cover', 'ANNUAL', 
                 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec', 
                 'avgjune', 'sub']

model = None
scaler = None
model_loaded = False
try:
    if os.path.exists('models/floods.save') and os.path.exists('models/transform.save'):
        model = joblib.load('models/floods.save')
        scaler = joblib.load('models/transform.save')
        model_loaded = True
        logger.info("Model loaded from 'models/' folder")
    elif os.path.exists('floods.save') and os.path.exists('transform.save'):
        model = joblib.load('floods.save')
        scaler = joblib.load('transform.save')
        model_loaded = True
        logger.info("Model loaded from root folder")
    else:
        logger.error("Model files not found! Please run train.py first")        
    if model_loaded:
        logger.info(f"Model Type: {type(model).__name__}")
        logger.info(f"Features: {len(FEATURE_NAMES)}")        
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model_loaded = False
def predict_flood(values):
    try:
        if model is None or scaler is None:
            return 0, 15
        values_array = np.array(values).reshape(1, -1)
        scaled = scaler.transform(values_array)
        pred = model.predict(scaled)[0]
        proba = model.predict_proba(scaled)[0]
        probability = int(proba[1] * 100) if pred == 1 else int(proba[0] * 100)
        return int(pred), probability
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return 0, 15
@app.route('/')
def home():
    return render_template('home.html', model_loaded=model_loaded)
@app.route('/predict', methods=['GET'])
def predict_page():
    return render_template('index.html', model_loaded=model_loaded, features=FEATURE_NAMES)
@app.route('/chance')
def chance_page():
    return render_template('chance.html', 
                         probability=request.args.get('probability', '75'),
                         temp=request.args.get('temp', '0'),
                         humidity=request.args.get('humidity', '0'),
                         cloud_cover=request.args.get('cloud_cover', '0'),
                         annual=request.args.get('annual', '0'),
                         jan_feb=request.args.get('jan_feb', '0'),
                         mar_may=request.args.get('mar_may', '0'),
                         jun_sep=request.args.get('jun_sep', '0'),
                         oct_dec=request.args.get('oct_dec', '0'),
                         avgjune=request.args.get('avgjune', '0'),
                         sub=request.args.get('sub', '0'))
@app.route('/no_chance')
def no_chance_page():
    return render_template('no_chance.html',
                         probability=request.args.get('probability', '20'),
                         temp=request.args.get('temp', '0'),
                         humidity=request.args.get('humidity', '0'),
                         cloud_cover=request.args.get('cloud_cover', '0'),
                         annual=request.args.get('annual', '0'),
                         jan_feb=request.args.get('jan_feb', '0'),
                         mar_may=request.args.get('mar_may', '0'),
                         jun_sep=request.args.get('jun_sep', '0'),
                         oct_dec=request.args.get('oct_dec', '0'),
                         avgjune=request.args.get('avgjune', '0'),
                         sub=request.args.get('sub', '0'))
@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = []
        for name in FEATURE_NAMES:
            val = request.form.get(name, '0')
            try:
                values.append(float(val))
            except:
                values.append(0.0)        
        pred, prob = predict_flood(values)        
        result = {
            'probability': prob,
            'temp': values[0],
            'humidity': values[1],
            'cloud_cover': values[2],
            'annual': values[3],
            'jan_feb': values[4],
            'mar_may': values[5],
            'jun_sep': values[6],
            'oct_dec': values[7],
            'avgjune': values[8],
            'sub': values[9]
        }        
        if pred == 1:
            return redirect(url_for('chance_page', **result))
        else:
            return redirect(url_for('no_chance_page', **result))   
    except Exception as e:
        flash("An error occurred. Please try again.", "error")
        return redirect(url_for('predict_page'))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)