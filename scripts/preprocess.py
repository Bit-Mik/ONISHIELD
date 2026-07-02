import pandas as pd

# ----------------------------------
# Load Dataset
# ----------------------------------

df = pd.read_csv("sensor_data.csv")

print(f"Original Records : {len(df)}")

# ----------------------------------
# Remove Duplicate Records
# ----------------------------------

df.drop_duplicates(inplace=True)

# ----------------------------------
# Remove Missing Values
# ----------------------------------

df.dropna(inplace=True)

# ----------------------------------
# Convert Columns to Numeric
# ----------------------------------

df["Temperature"] = pd.to_numeric(
    df["Temperature"],
    errors="coerce"
)

df["Humidity"] = pd.to_numeric(
    df["Humidity"],
    errors="coerce"
)

df.dropna(inplace=True)

# ----------------------------------
# Remove Impossible Sensor Values
# ----------------------------------

df = df[
    (df["Temperature"] >= 0) &
    (df["Temperature"] <= 50)
]

df = df[
    (df["Humidity"] >= 20) &
    (df["Humidity"] <= 90)
]

# ----------------------------------
# Remove Noise using Moving Average
# ----------------------------------

df["Temperature"] = (
    df["Temperature"]
    .rolling(window=5, min_periods=1)
    .mean()
)

df["Humidity"] = (
    df["Humidity"]
    .rolling(window=5, min_periods=1)
    .mean()
)

# ----------------------------------
# Generate Initial Blower Labels
# ----------------------------------

def blower_speed(temp, hum):

    if temp >= 35 or hum >= 80:
        return 100

    elif temp >= 30 or hum >= 70:
        return 80

    elif temp >= 25 or hum >= 60:
        return 60

    else:
        return 30


df["BlowerSpeed"] = df.apply(
    lambda row:
    blower_speed(
        row["Temperature"],
        row["Humidity"]
    ),
    axis=1
)

# ----------------------------------
# Save Processed Dataset
# ----------------------------------

df.to_csv(
    "processed_data.csv",
    index=False
)

print(f"Processed Records : {len(df)}")
print(df.head())