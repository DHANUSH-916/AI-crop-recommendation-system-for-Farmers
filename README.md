# 🌱 AI Crop Recommendation System for Farmers

## Overview

The **AI Crop Recommendation System for Farmers** is a machine learning-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The system helps farmers make informed decisions, improve crop yield, and promote sustainable farming practices.

---

## Features

* 🤖 Machine Learning-based crop prediction
* 🌾 Recommends the most suitable crop
* 📊 Uses soil and environmental parameters
* 🌐 User-friendly web interface built with Flask
* ⚡ Fast and accurate predictions

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

---

## Dataset Features

The model uses the following input parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature (°C)
* Humidity (%)
* pH Value
* Rainfall (mm)

---

## Project Structure

```text
AI_Crop_Advanced_Web_App/
│
├── app.py
├── train_model.py
├── model.pkl
├── dataset.csv
├── requirements.txt
├── templates/
├── static/
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/DHANUSH-916/AI-crop-recommendation-system-for-Farmers.git
```

### Navigate to the project

```bash
cd AI-crop-recommendation-system-for-Farmers
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## How It Works

1. Enter soil nutrient values and environmental conditions.
2. The trained machine learning model processes the input.
3. The application predicts the most suitable crop.
4. The recommended crop is displayed instantly.

---

## Future Improvements

* Fertilizer recommendation
* Weather API integration
* Disease prediction
* Crop yield estimation
* Multi-language support
* Mobile-friendly interface

---

## Author

**Dhanush R**

* GitHub: https://github.com/DHANUSH-916

---

## License

This project is intended for educational and learning purposes.
