
# ❄️ Snowfall Prediction Web App  

## 🧠 Objective  
The objective of this project is to build a **machine learning model** that predicts whether there will be snowfall the next day based on weather conditions such as temperature, precipitation, and elevation. Using **Gaussian Naive Bayes**, the model helps forecast snowfall with high accuracy for better weather planning and safety decisions.

---

## 📊 Dataset Details  

### 1. **Summary of Weather.csv**  
Contains daily meteorological data with columns such as:  
- **Date** – Specific date of observation  
- **Precipitation** – Amount of rainfall/snowfall measured  
- **Temperature** – Recorded temperature of the day  
- **Poor Weather** – Indicates bad weather conditions  
- **Snowfall** – Target variable (Yes/No)

### 2. **Weather Station Locations.csv**  
Provides location details of weather stations:  
- **Station ID** – Unique identifier for each station  
- **Elevation** – Height of the station (important for snow likelihood)  
- **Latitude / Longitude** – Used for location-based mapping and analysis  

---

## 🧩 Model and Approach  

### ⚙️ Algorithm Used:  
**Gaussian Naive Bayes (GNB)**  
- Works efficiently with continuous features like temperature and precipitation.  
- Assumes normal distribution and calculates the probability of snowfall occurrence.  

### 🧠 Training:  
Two models were trained:  
- `nb_model_snowfall` → Predicts if **tomorrow will have snowfall**  
- `nb_model_poor_weather` → Predicts if **tomorrow will have poor weather**

**Training Accuracy:** `0.9581` (≈95.8%)  

---

## 🌐 Web Application  

### 🖥️ Tech Stack:
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask / FastAPI)  
- **Deployment:** Render  

### 🧾 Input Features:
| Feature | Description |
|----------|--------------|
| Precipitation | Rainfall/Snowfall amount |
| Temperature | Current temperature (°C) |
| Year | Year of prediction |
| Month | Month of prediction |
| Date | Day of the month |
| Elevation | Altitude of the location |

### 📈 Example Output:
> **Result:** NO (Tomorrow will not be snowfall)  

---

## 🚀 Deployment Link  
🔗 [Snowfall Prediction App on Render](https://snowfall-predict-app.onrender.com/)

---

## 🧾 Summary  
This project demonstrates the use of **Naive Bayes classification** for weather prediction using real meteorological datasets. The app provides an easy-to-use interface for users to check snowfall predictions based on entered parameters, supporting environmental forecasting and public awareness.

---

## 👨‍💻 Author  
**Prem Kumar**  
Data Science | Machine Learning | AI Enthusiast  


![Screenshot (38)](https://github.com/Premkumar9799817360/snowfall_prediction/assets/83695512/f5f2f9e6-a112-46b0-944b-c9e05f23136e)
# RESULT
![Screenshot (39)](https://github.com/Premkumar9799817360/snowfall_prediction/assets/83695512/fbb556dd-405a-4fd0-9d36-0bd66ddfffb1)
