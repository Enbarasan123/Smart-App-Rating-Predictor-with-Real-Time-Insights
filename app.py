import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from model import Model
from utils import generate_insight, shap_explanation, init_explainer
from database import init_db, save_prediction

app = Flask(__name__)
socketio = SocketIO(app)

# ================= INIT =================
model = Model()
df = model.load_and_train()
init_db()

# 🔥 Initialize SHAP
init_explainer(model.model, model.X_train)

# Analysis
top_apps = df.sort_values(by=['Installs','Rating'], ascending=False).head(10)
top_category = df['Category'].value_counts().idxmax()
peak_category = df.groupby('Category')['Installs'].sum().idxmax()
best_category = df.groupby('Category')['Rating'].mean().idxmax()

# ================= ROUTE =================
@app.route("/")
def home():

    categories = sorted(df['Category'].unique())

    category_data = df.groupby('Category')['Installs'].sum()\
        .sort_values(ascending=False).head(5)

    return render_template(
        "index.html",
        mae=model.mae,
        top_category=top_category,
        peak_category=peak_category,
        best_category=best_category,
        categories=categories,
        top_apps=top_apps.values.tolist(),
        category_labels=list(category_data.index),
        category_values=list(category_data.values),
        feature_names=model.features,
        feature_values=model.model.feature_importances_
    )

# ================= SOCKET =================
@socketio.on('predict_live')
def handle_prediction(data):

    reviews = int(data['reviews'])
    installs = int(data['installs'])
    price = float(data['price'])
    app_type = data['type']
    app_name = data.get('app_name', 'Unknown')

    pred, input_data = model.predict(reviews, installs, price, app_type)

    insight = generate_insight(reviews, installs, price, pred)

    # 🔥 SHAP explanation
    explanation = shap_explanation(input_data, model.features)

    # Save to DB
    save_prediction(app_name, reviews, installs, price, pred)

    emit('prediction_result', {
        'prediction': pred,
        'insight': insight,
        'explanation': explanation
    })

# ================= RUN =================
if __name__ == "__main__":
    socketio.run(app, debug=True)