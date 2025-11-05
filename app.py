from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open("iris.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    if request.method == "POST":
        # Get input from user
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])
        
        # Predict using model
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = result[0]

    return render_template("home.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
