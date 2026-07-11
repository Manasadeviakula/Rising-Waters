# Flood Prediction System

## Project Description

The Flood Prediction System is a Machine Learning based web application developed using Python and Flask. It predicts whether a flood is likely to occur based on rainfall and weather-related parameters.

## Features

- Data Loading
- Data Preprocessing
- Missing Value Handling
- Outlier Detection and Handling
- Feature Scaling
- Decision Tree Model
- Random Forest Model
- KNN Model
- XGBoost Model
- Model Comparison
- Flood Prediction using Flask

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib

## Project Structure

```
Flood-Prediction-System/

├── app.py
├── train.py
├── requirements.txt
├── README.md

├── dataset/
│   └── flood dataset.xlsx

├── models/
│   ├── floods.save
│   └── transform.save

├── templates/
│   └── index.html

├── static/
│   ├── css/
│   └── images/
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Model Training

```bash
python train.py
```

## Run Flask Application

```bash
python -m pip install joblib
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Machine Learning Models

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

## Final Model

XGBoost is selected as the final model based on its prediction accuracy.

## Author

Flood Prediction System Project
