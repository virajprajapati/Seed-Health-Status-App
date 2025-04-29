# 🥔 Seed Health Status App

A Streamlit-based machine learning web app to predict the **health status of potato seeds** inside a cold storage facility, based on environmental sensor readings.

## 🚀 Demo

🔗 [Launch the App on Streamlit](https://seed-health-status-app.streamlit.app/) *(Replace with actual link after deployment)*

---

## 📂 Project Structure

```
Seed-Health-Status-App/
├── app.py                # Streamlit frontend app
├── model.pkl             # Trained RandomForest model
├── requirements.txt      # Dependencies for Streamlit Cloud
├── good_health.png       # Image shown for Good health status
├── fair_health.png       # Image shown for Fair health status
├── poor_health.png       # Image shown for Poor health status
└── sensor_data.csv       # Optional: Raw sensor data for training
```

---

## 💡 Features

- Takes input from 3 key cold storage sensors:
  - 🌡 Temperature (°C)
  - 💧 Humidity (%)
  - 🫧 CO₂ Concentration (ppm)
- Predicts potato health as:
  - ✅ **Good**
  - ⚠️ **Fair**
  - ❌ **Poor**
- Visual health status image output

---

## 🛠 Built With

- [Streamlit](https://streamlit.io/) — for frontend
- [scikit-learn](https://scikit-learn.org/) — for ML model
- [pandas](https://pandas.pydata.org/) — for data handling
- [numpy](https://numpy.org/) — for numeric processing

---

## 🧠 Model Details

- Model: **RandomForestClassifier**
- Dataset: Simulated cold storage sensor data (`sensor_data.csv`)
- Features: `Temperature`, `Humidity`, `CO2`
- Target: `Health` (Good, Fair, Poor)

---

## 🔧 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/virajprajapati/Seed-Health-Status-App.git
cd Seed-Health-Status-App

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 📈 Future Improvements

- Live integration with real sensor devices (MQTT / REST API)
- Health prediction over time (time-series analysis)
- Dashboard analytics for warehouse monitoring

---

## 📬 Contact

👤 **Viraj Prajapati**  
📧 [virajprajapati62@gmail.com](mailto:virajprajapati62@gmail.com)