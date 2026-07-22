from flask import Flask, render_template, request
import pickle
import pandas as pd

# ==========================
# Fertilizer Recommendation
# ==========================

fertilizer = {
    "Rice": "Urea, DAP",
    "Maize": "Urea, MOP",
    "Wheat": "Urea, SSP",
    "Cotton": "NPK 20-20-0",
    "Sugarcane": "Urea, Potash",
    "Tomato": "NPK 19-19-19",
    "Onion": "DAP, Potash",
    "Potato": "Urea, Potash",
    "Brinjal": "NPK 10-26-26",
    "Chilli": "DAP, NPK"
}

# ==========================
# Crop Information
# ==========================

crop_info = {

    "Rice": {
        "description": "Rice is one of the world's most important cereal crops and grows best in warm and humid climates.",
        "temperature": "20°C - 35°C",
        "rainfall": "1200 - 2000 mm",
        "water": "High",
        "soil": "Clay Soil",
        "season": "Kharif"
    },

    "Maize": {
        "description": "Maize is a cereal crop widely grown for food, fodder and industrial use.",
        "temperature": "18°C - 27°C",
        "rainfall": "500 - 800 mm",
        "water": "Moderate",
        "soil": "Well-drained Loamy Soil",
        "season": "Kharif"
    },

    "Wheat": {
        "description": "Wheat is one of the most widely cultivated cereal crops.",
        "temperature": "15°C - 25°C",
        "rainfall": "500 - 1000 mm",
        "water": "Moderate",
        "soil": "Loamy Soil",
        "season": "Rabi"
    },

    "Cotton": {
        "description": "Cotton is a major fibre crop grown in warm climates.",
        "temperature": "21°C - 30°C",
        "rainfall": "600 - 1200 mm",
        "water": "Moderate",
        "soil": "Black Soil",
        "season": "Kharif"
    },

    "Sugarcane": {
        "description": "Sugarcane is a tropical crop used for sugar production.",
        "temperature": "20°C - 35°C",
        "rainfall": "1000 - 1500 mm",
        "water": "High",
        "soil": "Deep Loamy Soil",
        "season": "Annual"
    },

    "Tomato": {
        "description": "Tomato is one of the most popular vegetable crops.",
        "temperature": "18°C - 27°C",
        "rainfall": "400 - 600 mm",
        "water": "Moderate",
        "soil": "Well-drained Sandy Loam",
        "season": "Year Round"
    },

    "Onion": {
        "description": "Onion is an important vegetable crop grown throughout India.",
        "temperature": "13°C - 25°C",
        "rainfall": "350 - 550 mm",
        "water": "Low to Moderate",
        "soil": "Loamy Soil",
        "season": "Rabi"
    },

    "Potato": {
        "description": "Potato is a cool-season tuber crop.",
        "temperature": "15°C - 20°C",
        "rainfall": "500 - 700 mm",
        "water": "Moderate",
        "soil": "Sandy Loam",
        "season": "Rabi"
    },

    "Brinjal": {
        "description": "Brinjal (Eggplant) is grown throughout the year in warm regions.",
        "temperature": "22°C - 30°C",
        "rainfall": "600 - 1000 mm",
        "water": "Moderate",
        "soil": "Fertile Loamy Soil",
        "season": "Year Round"
    },

    "Chilli": {
        "description": "Chilli is an important spice crop cultivated across India.",
        "temperature": "20°C - 30°C",
        "rainfall": "600 - 1200 mm",
        "water": "Moderate",
        "soil": "Well-drained Sandy Loam",
        "season": "Kharif"
    }

}

# ==========================
# Flask App
# ==========================

app = Flask(__name__)

model, columns, acc = pickle.load(open("model.pkl", "rb"))

# ==========================
# Home Route
# ==========================

@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    fert = None
    probs = None
    info = None

    if request.method == "POST":

        values = [float(request.form[x]) for x in columns]

        df = pd.DataFrame([values], columns=columns)

        result = model.predict(df)[0]

        fert = fertilizer.get(result, "Recommended fertilizer not available.")

        probabilities = model.predict_proba(df)[0]

        probs = sorted(
            zip(model.classes_, probabilities),
            key=lambda x: x[1],
            reverse=True
        )

        info = crop_info.get(result, {

            "description": "Information not available.",
            "temperature": "-",
            "rainfall": "-",
            "water": "-",
            "soil": "-",
            "season": "-"

        })

    return render_template(

        "index.html",

        result=result,

        fert=fert,

        probs=probs,

        crop_info=info,

        acc=round(acc * 100, 2)

    )


# ==========================
# Run App
# ==========================

if __name__ == "__main__":
    app.run(debug=True)