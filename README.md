# 🏦 Loan Approval Prediction App

A Machine Learning web application that predicts whether a loan will be approved or not based on applicant details.
This project is built using **Gaussian Naive Bayes**, deployed using **Streamlit**, and trained in Jupyter Notebook.

---

## 📌 Project Overview

This project predicts loan approval status using applicant features such as:

* Gender
* Marital Status
* Dependents
* Education
* Applicant Income
* Loan Amount
* Credit History
* And other features

The model was trained on a dataset with **27 input features**.

---

## 🧠 Machine Learning Model

* Algorithm Used: **Gaussian Naive Bayes**
* Library: `scikit-learn`
* Model saved using: `joblib`
* Input Features: 27
* Output: Loan Approved (1) / Rejected (0)

---

## 🛠 Tech Stack

* Python
* Jupyter Notebook
* Streamlit
* Scikit-learn
* NumPy
* Pandas
* Joblib

---

## 📂 Project Structure

```
Loan_Approval_Project/
│
├── loan_approval.ipynb      # Model training notebook
├── app.py                   # Streamlit web application
├── model.pkl                # Saved trained model
├── requirements.txt         # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/loan-approval-app.git
cd loan-approval-app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

App will run on:

```
http://localhost:8501
```

---

## 🌍 Deployment

This project is deployed using **Streamlit Community Cloud**.

Steps to deploy:

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repository
4. Select `app.py`
5. Click Deploy

---

## 📊 Model Training

The model was trained using:

* Data preprocessing
* Feature selection
* Train-test split
* Gaussian Naive Bayes classifier

Model saved using:

```python
import joblib
joblib.dump(model, "model.pkl")
```

---

## 👨‍💻 Author

**Saurav Kumar Verma**
AI/ML Enthusiast | Full Stack Developer

---

## ⭐ If You Like This Project

Give this repository a star ⭐ on GitHub!
