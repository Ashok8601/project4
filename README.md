
## 🌸 Iris Flower Species Prediction using Flask and Machine Learning

### 🧠 Overview

This project demonstrates how to **deploy a Machine Learning model using Flask**.
The trained model (`iris.pkl`) predicts the **species of an Iris flower** based on its physical measurements:

* **Sepal Length (cm)**
* **Sepal Width (cm)**
* **Petal Length (cm)**
* **Petal Width (cm)**

It uses a simple web interface built with **HTML and CSS**, where users can input the flower's details and instantly get a predicted species output.

---

## 📁 Project Structure

```
iris_project/
│
├── app.py                # Main Flask backend
├── iris.pkl              # Trained ML model (saved using pickle)
├── requirements.txt      # All required dependencies
└── templates/
    └── home.html         # Frontend HTML form
```

---

## 🧩 How It Works

1. **Model Training (Offline):**

   * A Logistic Regression or Decision Tree model is trained using the **Iris dataset** from scikit-learn.
   * The trained model is saved as `iris.pkl` using the Python `pickle` library.

2. **Model Loading (Online):**

   * The Flask app (`app.py`) loads this `.pkl` file at runtime.
   * User input values are passed into `model.predict()` to get the predicted species.

3. **Frontend Interaction:**

   * The HTML form collects the four input values.
   * When the user clicks **Predict**, data is sent to Flask via POST request.
   * Flask returns the predicted **Iris species** (e.g., *Setosa*, *Versicolor*, or *Virginica*).

---

## ⚙️ Installation Steps

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ashok8601/project4/
cd project4
```

### 2️⃣ Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For Linux/Mac
```

### 3️⃣ Install Dependencies

Create a file named `requirements.txt` with this content:

```
flask
scikit-learn
pickle-mixin
```

Then run:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Example Input & Output

| Input Features                                                                     | Predicted Output |
| ---------------------------------------------------------------------------------- | ---------------- |
| Sepal Length = 5.1<br>Sepal Width = 3.5<br>Petal Length = 1.4<br>Petal Width = 0.2 | **Setosa**       |
| Sepal Length = 6.0<br>Sepal Width = 2.7<br>Petal Length = 5.1<br>Petal Width = 1.6 | **Versicolor**   |

---

## 💾 Model Saving Code Example

```python
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load data and train model
data = load_iris()
X, y = data.data, data.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the model
with open("iris.pkl", "wb") as file:
    pickle.dump(model, file)
```

---

## 💻 Technologies Used

| Component        | Description                              |
| ---------------- | ---------------------------------------- |
| **Flask**        | Python micro web framework for backend   |
| **scikit-learn** | For training and predicting iris dataset |
| **HTML/CSS**     | For frontend form and display            |
| **Pickle**       | For saving and loading the trained model |

---

## 🧑‍🏫 Learning Outcomes

* How to **train, serialize, and deploy** a machine learning model using Flask.
* How to create **interactive web forms** that accept user input.
* Understanding the **workflow between ML model and Flask backend**.

---

## 🌐 Future Improvements

* Add model retraining functionality.
* Create a database to save prediction history.
* Deploy the app on cloud platforms like **Render**, **Railway**, or **Heroku**.

---

## 🏁 Conclusion

This project is a simple yet powerful demonstration of how Machine Learning models can be deployed into production environments using Flask.
It bridges the gap between **data science and web development**, allowing real users to interact with AI models through a browser.

---

Would you like me to also generate a short version of this `README.md` (for quick display on GitHub profile or portfolio)?
