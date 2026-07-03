import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
data = pd.read_csv("aqi.csv")

# Features and Target
X = data[["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]]
y = data["AQI"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

print("====== AQI FORECAST SYSTEM ======")

pm25 = float(input("Enter PM2.5: "))
pm10 = float(input("Enter PM10: "))
no2 = float(input("Enter NO2: "))
so2 = float(input("Enter SO2: "))
co = float(input("Enter CO: "))
o3 = float(input("Enter O3: "))

prediction = model.predict([[pm25, pm10, no2, so2, co, o3]])[0]

print("\nPredicted AQI:", round(prediction, 2))

if prediction <= 50:
    print("Category : Good")
elif prediction <= 100:
    print("Category : Satisfactory")
elif prediction <= 200:
    print("Category : Moderate")
elif prediction <= 300:
    print("Category : Poor")
elif prediction <= 400:
    print("Category : Very Poor")
else:
    print("Category : Severe")
