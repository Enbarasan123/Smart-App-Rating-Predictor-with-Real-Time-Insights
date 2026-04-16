import shap
import numpy as np

# Load explainer once (performance)
explainer = None

def init_explainer(model, X_train):
    global explainer
    explainer = shap.Explainer(model, X_train)


def generate_insight(reviews, installs, price, pred):
    insight = ""

    if installs > 1000000:
        insight += "📈 High installs indicate strong demand. "

    if reviews > 50000:
        insight += "💬 High engagement detected. "

    if price == 0:
        insight += "🆓 Free apps attract more users. "

    if pred > 4.2:
        insight += "🔥 Excellent success potential."
    elif pred > 3.5:
        insight += "👍 Good performance expected."
    else:
        insight += "⚠️ Needs improvement."

    return insight


# 🔥 SHAP EXPLANATION
def shap_explanation(input_data, feature_names):
    global explainer

    shap_values = explainer(input_data)

    explanation = []

    for i, value in enumerate(shap_values.values[0]):
        if abs(value) > 0.1:
            impact = "increased" if value > 0 else "decreased"
            explanation.append(
                f"{feature_names[i]} {impact} the prediction significantly"
            )

    if not explanation:
        explanation.append("All features have balanced influence")

    return explanation