import joblib

model = joblib.load(

    "blower_model.pkl"

)

temperature = float(

    input(

        "Temperature : "

    )

)

humidity = float(

    input(

        "Humidity : "

    )

)

prediction = model.predict(

    [

        [

            temperature,

            humidity

        ]

    ]

)

blower = int(

    prediction[0]

)

blower = max(

    0,

    min(

        blower,

        100

    )

)

print()

print(

    "Predicted Blower Speed =",

    blower,

    "%"

)