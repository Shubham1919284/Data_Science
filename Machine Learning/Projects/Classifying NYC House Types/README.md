# Room Type Predictor · NYC Airbnb 🗽🏠

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-009688.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E.svg)
![HTML/CSS/JS](https://img.shields.io/badge/Frontend-Vanilla_JS-E34F26.svg)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7.svg)

A full-stack machine learning application that predicts the room type of an Airbnb listing in New York City based on various listing characteristics. The project combines a **Random Forest Classifier** with a robust **FastAPI** backend and a sleek, modern **Vanilla JS** frontend.

---

## 🚀 Live Demo

- **Frontend (Static Site):** [Live Site](https://room-type-predictor-nyc-airbnb-1.onrender.com)
- **Backend (Web Service):** [API Root](https://room-type-predictor-nyc-airbnb.onrender.com) / [API Docs](https://room-type-predictor-nyc-airbnb.onrender.com/docs)

---

## ✨ Features

- **Real-time Prediction**: Classifies NYC Airbnb listings into specific room types using a pre-trained Random Forest model.
- **Dynamic Frontend**: Modern, responsive, and glassmorphic user interface to input listing properties interactively.
- **Robust REST API**: Built with FastAPI, utilizing Pydantic for strict input validation.
- **Comprehensive ML Pipeline**: Includes a fully contained Jupyter Notebook detailing the exploratory data analysis, data cleaning, and model training processes.
- **Cross-Origin Resource Sharing (CORS)**: Configured seamlessly to allow the frontend to communicate with the deployed backend.

---

## 🛠️ Tech Stack

### Machine Learning
- **scikit-learn**: Random Forest Classifier implementation
- **pandas**: Data manipulation and preprocessing
- **joblib**: Model serialization and loading
- **Jupyter Notebook**: Data exploration and model training (`Room_Type_Predictor_NYC_Airbnb.ipynb`)

### Backend
- **FastAPI**: High-performance asynchronous REST API framework
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server

### Frontend
- **HTML5 / CSS3**: Space Grotesk, Inter, and JetBrains Mono fonts for a premium aesthetic
- **Vanilla JavaScript**: API integration and DOM manipulation

---

## 📂 Project Structure

```text
├── .gitignore
├── Room_Type_Predictor_NYC_Airbnb.ipynb  # ML Notebook (EDA, preprocessing, training)
├── index.html                            # Frontend Entry Point
├── main.py                               # FastAPI Application Backend
├── model_pipeline.pkl                    # Serialized Random Forest Model Pipeline
├── requirements.txt                      # Python Dependencies
├── runtime.txt                           # Python version specification
├── script.js                             # Frontend JavaScript Logic
└── style.css                             # Frontend Styles
```

---

## 🧠 Machine Learning Overview

The core of this application is a **Random Forest Classifier**.
The model considers the following features to determine the predicted room type:
- **Location**: `neighbourhood_group` (Borough), `neighbourhood`, `latitude`, `longitude`
- **Pricing & Stay Constraints**: `price`, `minimum_nights`, `availability_365`
- **Host & Reviews**: `number_of_reviews`, `reviews_per_month`, `calculated_host_listings_count`

The complete training pipeline, including feature engineering and cross-validation, is documented in the `Room_Type_Predictor_NYC_Airbnb.ipynb` notebook.

---

## 💻 Local Setup & Installation

### Prerequisites
- Python 3.10+
- Git

### 1. Clone the repository
```bash
git clone https://github.com/Shubham1919284/Room-Type-Predictor---NYC-Airbnb.git
cd Room-Type-Predictor---NYC-Airbnb
```

### 2. Set up the Python virtual environment
```bash
python -m venv .venv
source .venv/bin/activate    # On Windows use: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Backend
```bash
uvicorn main:app --reload
```
The backend will be available at `http://localhost:8000`. You can test the endpoints via the Swagger UI at `http://localhost:8000/docs`.

### 5. Run the Frontend
Simply open the `index.html` file in your preferred web browser, or use a local development server (like VS Code Live Server or Python's `http.server`):
```bash
python -m http.server 3000
```
Then navigate to `http://localhost:3000`.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/` | Root endpoint, returns API status and helpful links. |
| `GET`  | `/health` | Health check endpoint for deployment monitoring. |
| `POST` | `/predict` | Main inference endpoint. Expects a JSON payload of listing features and returns the predicted room type and class probabilities. |

*For detailed schema definitions, check the `/docs` endpoint of the live backend.*

---

## ☁️ Deployment Details

The application is fully configured for automated deployment on **Render**:
- **Backend**: Deployed as a Python 3 Web Service (`srv-d9ueffegekts73dt6eg0`).
- **Frontend**: Deployed as a Static Site (`srv-d9unh4h5efls73d236ng`).

The CORS settings in `main.py` are explicitly tailored to allow requests from the deployed frontend URL (`https://room-type-predictor-nyc-airbnb-1.onrender.com`).
