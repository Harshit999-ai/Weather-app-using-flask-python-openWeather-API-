# Weather-app-using-flask-python-openWeather-API-
# 🌦️ Weather App (Flask + OpenWeatherMap API)

A simple and clean weather web application built using **Flask** that fetches real-time weather data using the **OpenWeatherMap (OWM) API**.

---

## 🚀 Features

* 🔍 Search weather by city name
* 🌡️ Real-time temperature, humidity, and conditions
* ⚡ Fast and lightweight Flask backend
* 🎨 Clean and responsive UI
* ❌ Error handling for invalid city names
* 🌙 Optional dark mode support (if implemented)

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS (Bootstrap optional)
* **API:** OpenWeatherMap API

---

## 📸 Screenshots

> Add your app screenshots here

```
Example:
![Home Page](screenshots/home.png)
![Result Page](screenshots/result.png)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get your API key

* Go to [https://openweathermap.org/api](https://openweathermap.org/api)
* Sign up and generate your API key

### 5. Configure environment variables

Create a `.env` file in the root directory:

```env
API_KEY=your_openweathermap_api_key
```

---

## ▶️ Run the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
weather-app/
│── app.py
│── requirements.txt
│── .env
│── templates/
│   └── index.html
│── static/
│   └── style.css
```

---

## 🧠 Learning Goals

This project helps you understand:

* How to build a Flask web app
* How to integrate third-party APIs
* Handling user input and errors
* Rendering dynamic data with Jinja2

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💡 Future Improvements

* 📍 Detect user location automatically
* 📊 Add weather charts/graphs
* 📱 Improve mobile responsiveness
* 🌐 Deploy on cloud (Render / Vercel / AWS)

---

## ⭐ Show Your Support

If you like this project, consider giving it a ⭐ on GitHub!
