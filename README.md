# Smart-App-Rating-Predictor-with-Real-Time-Insights
A real-time AI-powered web app that predicts mobile app ratings and explains predictions using SHAP (Explainable AI)
# 🚀 Real-Time App Market Rating Predictor using Explainable AI

This project is a **Real-Time App Market Prediction System** that uses **Machine Learning, Flask, and Explainable AI (SHAP)** to predict mobile app ratings and analyze market trends.

---

## 📌 Overview

The application predicts app ratings based on key features such as:

* Reviews
* Installs
* Price
* App Type (Free/Paid)

It also provides **real-time predictions**, **insights**, and **feature explanations** to help understand app success in the market.

A `README.md` file is the main documentation file in a project that explains what the project does, how to use it, and why it is useful ([GeeksforGeeks][1])

---

## ✨ Features

* ⚡ Real-time prediction using Flask-SocketIO
* 🤖 Machine Learning model (Gradient Boosting Regressor)
* 🧠 Explainable AI using SHAP
* 📊 Market analysis (top apps, categories)
* 💡 Smart insights generation
* 💾 Database storage for predictions
* 📈 Feature importance visualization
 🧠 Machine Learning

* Model: Gradient Boosting Regressor
* Features used:

  * Reviews
  * Installs
  * Price
  * Type
* Evaluation Metric: Mean Absolute Error (MAE)

🛠️ Tech Stack

* **Backend:** Flask, Flask-SocketIO
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Explainability:** SHAP
* **Database:** SQLite
* **Frontend:** HTML, Jinja Templates

---

## 📁 Project Structure

```
project/
│── app.py
│── model.py
│── utils.py
│── database.py
│── templates/
│   └── index.html
│── static/
│── google_play_store_dataset.csv
│── README.md
 ⚙️ Installation & Setup

 1. Clone Repository

git clone https://github.com/your-username/app-market-predictor.git
cd app-market-predictor
2. Install Dependencies

pip install flask flask-socketio pandas numpy scikit-learn shap
3. Run Application


python app.py
 4. Open Browser
http://127.0.0.1:5000/
 🔮 How It Works

1. User inputs app details (reviews, installs, price, type)
2. Model predicts app rating
3. SHAP explains feature contribution
4. Insights are generated automatically
5. Results are displayed in real-time
 📊 Example Output

* ⭐ Predicted Rating: 4.3
* 💡 Insight: High installs indicate strong demand
* 🧠 Explanation: Installs increased prediction significantly
🚀 Future Improvements

* Add advanced models (XGBoost, Neural Networks)
* Deploy on cloud (Render / AWS)
* Improve UI with charts and dashboards
* Add user authentication

## 👨‍💻 Author

**Enbarasan**



