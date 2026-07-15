import joblib
import pandas as pd

lr = joblib.load("./model/linear_regression_model.pkl")
dt = joblib.load("./model/decision_tree_model.pkl")
rf = joblib.load("./model/random_forest_model.pkl")

features = joblib.load("./model/feature_list.pkl")

print("WELCOME TO DIAMOND PRICE PREDICTION APP WITH DEFINITLY THE BEST UI and THE BEST MODEL")

fts = ["carat", "cut", "color", "clarity", "depth", "table", "x", "y", "z"]
numeric = {"carat", "depth", "table", "x", "y", "z"}

diamond = {}
for ft in fts:
    x = input(f"Enter value for {ft}: ")
    if ft in numeric: 
        diamond[ft] = float(x)
    else:
        diamond[ft] = x

df = pd.DataFrame([diamond])
df_transformed = pd.get_dummies(df)
df_transformed = df_transformed.reindex(columns=features, fill_value=0)

prediction_lr = lr.predict(df_transformed)
prediction_dt = dt.predict(df_transformed)
prediction_rf = rf.predict(df_transformed)

print("\n\n")

print(f"Predicted Price with Linear Regression (Estimate): ${prediction_lr[0]:.2f}")
print(f"Predicted Price with Decision Tree (Likely Overfit, may not be accurate): ${prediction_dt[0]:.2f}")
print(f"Predicted Price with Random Forest (Very Accurate): ${prediction_rf[0]:.2f}")