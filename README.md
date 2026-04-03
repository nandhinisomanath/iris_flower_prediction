# 🌸 Iris Flower Classification
### Machine Learning Classification Project

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4.2-orange?style=flat-square&logo=scikit-learn)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green?style=flat-square&logo=fastapi)
![Dataset](https://img.shields.io/badge/Dataset-150%20rows-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 📌 Project Overview

This project builds a **multiclass classification model** to predict the species of an Iris flower — **Setosa, Versicolor, or Virginica** — based on its sepal and petal measurements.

The dataset contains **150 records** with **4 features** and is one of the most well-known beginner datasets in machine learning.

---

## 🎯 Problem Statement

> **"Can we predict the species of an Iris flower from its sepal length, sepal width, petal length, and petal width?"**

- **Target Variable** : `species` (Setosa / Versicolor / Virginica)
- **Task Type**       : Multiclass Classification
- **Dataset Size**    : 150 rows × 4 features
- **Source**          : [Kaggle / UCI / sklearn built-in](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)

---

## 📁 Project Structure

```
iris-ml-project/
│
├── notebooks/
│   └── iris_classification.ipynb    # Main ML notebook (all phases)
│
├── app/
│   └── main.py                      # FastAPI deployment app
│
├── models/
│   ├── iris_classifier.pkl          # Trained model
│   ├── iris_scaler.pkl              # StandardScaler
│   └── class_names.pkl              # Class name mapping
│
├── data/
│   └── iris.csv                     # Dataset
│
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 📊 Dataset Description

| Column | Type | Range | Description |
|---|---|---|---|
| `sepal length (cm)` | Float | 4.3 – 7.9 | Length of the sepal |
| `sepal width (cm)`  | Float | 2.0 – 4.4 | Width of the sepal  |
| `petal length (cm)` | Float | 1.0 – 6.9 | Length of the petal |
| `petal width (cm)`  | Float | 0.1 – 2.5 | Width of the petal  |
| `species`           | String | 3 classes | Target variable     |

### Class Distribution

| Class | Count | Percentage |
|---|---|---|
| Iris-setosa     | 50 | 33.3% |
| Iris-versicolor | 50 | 33.3% |
| Iris-virginica  | 50 | 33.3% |

> Perfectly balanced dataset — no class imbalance issue.

---

## 🔍 Key EDA Findings

- **Petal length** and **petal width** are the strongest features to separate all 3 species
- **Setosa** is very easy to separate from the other two — it has much smaller petals
- **Versicolor** and **Virginica** overlap slightly — slightly harder to distinguish
- All 4 features show clear differences across species in box plots

---

## ⚙️ Project Phases

| Phase | Description |
|---|---|
| **Phase 1** | Load dataset and understand structure |
| **Phase 2** | Exploratory Data Analysis — pairplot, boxplot, heatmap |
| **Phase 3** | Preprocessing — encode labels, scale features, train/test split |
| **Phase 4** | Train and compare 4 models |
| **Phase 5** | Evaluate best model — confusion matrix, classification report |
| **Phase 6** | Save model artifacts and predict on new data |
| **Phase 7** | Deploy as FastAPI REST endpoint |

---

## 🤖 Models Trained & Compared

| Model | Expected Accuracy |
|---|---|
| K-Nearest Neighbors (k=5) | ~96–97% |
| Support Vector Machine    | ~97–100% |
| Decision Tree             | ~93–96% |
| Logistic Regression       | ~96–97% |

> **SVM** was selected as the final model — highest accuracy on this dataset.

---

## 📈 Final Model Performance

**Model : Support Vector Machine (SVM)**

| Class | Precision | Recall | F1-Score |
|---|---|---|---|
| Iris-setosa     | 1.00 | 1.00 | 1.00 |
| Iris-versicolor | 0.94 | 1.00 | 0.97 |
| Iris-virginica  | 1.00 | 0.93 | 0.96 |
| **Weighted Avg**| **0.98** | **0.97** | **0.98** |

```
Test Accuracy : ~97–100%
```

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/nandhinisomanath/iris_flower_prediction.git
cd iris_flower_prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

```bash
jupyter notebook notebooks/EDA.ipynb
```

### 4. Start the API

```bash
uvicorn app.main:app --reload --port 8000
```

### 5. Open Swagger UI

```
http://localhost:8000/docs
```

---

## 🌐 API Usage

### Predict Flower Species

**Endpoint** : `POST /predict`

**Request Body :**
```json
{
  "sepal length (cm)": 5.1,
  "sepal width (cm)":  3.5,
  "petal length (cm)": 1.4,
  "petal width (cm)":  0.2
}
```

**Response :**
```json
{
  "prediction":  "Iris-setosa",
  "class_index": 0
}
```

### Health Check

**Endpoint** : `GET /`

```json
{
  "message": "Welcome to the Iris Classifier API"
}
```

---

## 📦 Requirements

```
pandas==2.2.2
numpy==1.26.4
matplotlib==3.8.4
seaborn==0.13.2
scikit-learn==1.4.2
joblib==1.4.2
fastapi==0.111.0
uvicorn==0.29.0
pydantic==2.7.1
```

---

## 🧠 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+  | Core language         |
| Pandas        | Data manipulation     |
| Matplotlib & Seaborn | Visualization  |
| Scikit-Learn  | ML models & metrics   |
| Joblib        | Model serialization   |
| FastAPI       | REST API deployment   |
| Uvicorn       | ASGI server           |

---

## 🔗 Source Code

The complete source code for this project is publicly available on GitHub.

| | |
|---|---|
| **Repository** | `iris_flower_prediction` |
| **GitHub Link** | `https://github.com/nandhinisomanath/iris_flower_prediction` |
| **Visibility**  | Public |

---

## 📌 How to Contribute

1. Fork the repository
2. Create a new branch → `git checkout -b feature/your-feature`
3. Commit your changes → `git commit -m "Add your feature"`
4. Push to branch → `git push origin feature/your-feature`
5. Open a Pull Request

---



## 👤 Author

**Your Name**
- GitHub   : [@nandhinisomanath](https://github.com/nandhinisomanath)
- Email    : nandhinisomanath03@gmail.com

---

> ⭐ If this project helped you, please give it a star on GitHub!