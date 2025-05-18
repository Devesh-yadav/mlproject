# 🎯 Student Math Score Predictor

This is a machine learning web application that predicts a student's math score based on input features. The project uses multiple regressors from **scikit-learn**, is wrapped in a **Flask** app, and is deployed on **AWS Elastic Beanstalk** with automated CI/CD via **AWS CodePipeline** and **GitHub**.

---

## 🚀 Key Features

- Trains multiple regression models with hyperparameter tuning  
- Custom logging and exception handling  
- Final model saved as `.pkl` using `joblib`  
- Flask-based web app for predictions  
- Deployed with Elastic Beanstalk + CodePipeline (auto-deploy on Git push)

---

## 🧱 Project Structure

mlproject/
├── src/ # Training, prediction, and utility code
├── notebook/ # EDA and model experimentation
├── templates/ # HTML template for web UI
├── application.py # Flask app entry point
├── requirements.txt # Dependencies
├── setup.py # Setup for packaging
└── .ebextensions/ # EB configuration


---

## ⚙️ Run Locally

```bash
git clone https://github.com/Devesh-yadav/mlproject.git
cd mlproject

pip install -r requirements.txt
python application.py
