import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

class Model:

    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.mae = None
        self.features = ['Reviews','Installs','Price','Type']
        self.X_train = None  # 🔥 needed for SHAP

    def load_and_train(self):

        df = pd.read_csv("google_play_store_dataset.csv")
        df = df.dropna()

        df['Reviews'] = df['Reviews'].astype(int)
        df['Installs'] = df['Installs'].str.replace('+','', regex=False)
        df['Installs'] = df['Installs'].str.replace(',','', regex=False).astype(int)
        df['Price'] = df['Price'].str.replace('$','', regex=False).astype(float)
        df['Type'] = df['Type'].map({'Free':0,'Paid':1})

        X = df[self.features]
        y = df['Rating']

        X_scaled = self.scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        self.X_train = X_train  # 🔥 store for SHAP

        self.model = GradientBoostingRegressor()
        self.model.fit(X_train, y_train)

        preds = self.model.predict(X_test)
        self.mae = round(mean_absolute_error(y_test, preds), 3)

        return df

    def predict(self, reviews, installs, price, app_type):
        type_encoded = 0 if app_type == "Free" else 1
        data = self.scaler.transform([[reviews, installs, price, type_encoded]])
        pred = self.model.predict(data)[0]
        return round(pred, 2), data