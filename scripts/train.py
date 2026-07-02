import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ----------------------------------
# Load Dataset
# ----------------------------------

print("Loading processed dataset...")

df = pd.read_csv("processed_data.csv")

print(f"Total Samples : {len(df)}")

# ----------------------------------
# Features & Target
# ----------------------------------

X = df[["Temperature", "Humidity"]]

y = df["BlowerSpeed"]

# ----------------------------------
# Train-Test Split
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# ----------------------------------
# Train Model
# ----------------------------------

print("\nTraining Linear Regression Model...")

model = LinearRegression()

model.fit(X_train, y_train)

print("Training Complete.")

# ----------------------------------
# Save Model
# ----------------------------------

joblib.dump(model, "blower_model.pkl")

print("\nModel Saved Successfully.")

# ----------------------------------
# Print Equation
# ----------------------------------

print("\n========== MODEL ==========")

print(f"Intercept : {model.intercept_:.3f}")

print(f"Temperature Coefficient : {model.coef_[0]:.3f}")

print(f"Humidity Coefficient    : {model.coef_[1]:.3f}")

print(
    f"\nBlower Speed = "
    f"{model.coef_[0]:.3f} × Temperature + "
    f"{model.coef_[1]:.3f} × Humidity + "
    f"({model.intercept_:.3f})"
)