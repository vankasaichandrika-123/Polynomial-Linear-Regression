# Polynomial-Linear-Regression
# Polynomial Linear Regression - Salary Prediction

## 📌 Project Overview

This project predicts employee salaries based on their position level using **Polynomial Linear Regression**. Since the relationship between position level and salary is nonlinear, Polynomial Regression provides more accurate predictions than Simple Linear Regression.

---

## 🚀 Features

- Predict Salary based on Position Level
- Polynomial Linear Regression Model
- Flask Web Application
- User-friendly Web Interface
- Model saved using Pickle
- Ready for Render Deployment

---

## 📂 Project Structure

```
Polynomial_Linear_Regression/
│
├── app.py
├── Position_Salaries.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    └── index.html
```

---

## 📊 Dataset

Dataset Name:

**Position_Salaries.csv**

Columns:

- Position
- Level
- Salary

Example:

| Position | Level | Salary |
|----------|------:|--------:|
| Business Analyst | 1 | 45000 |
| Junior Consultant | 2 | 50000 |
| Senior Consultant | 3 | 60000 |
| Manager | 4 | 80000 |
| Country Manager | 5 | 110000 |
| Region Manager | 6 | 150000 |
| Partner | 7 | 200000 |
| Senior Partner | 8 | 300000 |
| C-level | 9 | 500000 |
| CEO | 10 | 1000000 |

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS
- Bootstrap
- Pickle

---

## 📈 Machine Learning Algorithm

- Polynomial Linear Regression

Libraries Used:

- PolynomialFeatures
- LinearRegression

---

## ⚙ Installation

Clone Repository

```bash
git clone https://github.com/vankasaichandrik-123/Polynomial_Linear_Regression.git
```

Go to Project Folder

```bash
cd Polynomial_Linear_Regression
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Flask Application

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

## 💻 Input

Enter Position Level

Example:

```
6.5
```

---

## 📤 Output

Example

```
Predicted Salary

₹ 174878.08
```

---

## 📦 Model

Model File

```
Position_Salaries.pkl
```

Saved Using

```python
import pickle

with open("Position_Salaries.pkl","wb") as f:
    pickle.dump((poly, reg), f)
```

---

## 🌐 Deployment

Deploy using

- Render
- GitHub

Start Command

```
gunicorn app:app
```

---

## 📷 Application

### Home Page

- Enter Position Level
- Click Predict Salary

### Prediction Page

Displays predicted salary instantly.

---

## 👩‍💻 Developed By

**Vanka Saichandrika**

Data Scientist | Machine Learning Enthusiast

---

## ⭐ Future Enhancements

- Add graphs and visualization
- Upload CSV for batch prediction
- Responsive UI
- Docker Support
- Cloud Deployment

---

## 📜 License

This project is developed for educational and learning purposes.
