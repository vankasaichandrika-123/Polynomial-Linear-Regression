from flask import Flask, render_template, request
import numpy as np
import pickle
import sys

app = Flask(__name__)

# ==========================================
# Load Model
# ==========================================

try:
    with open("Position_Salaries.pkl", "rb") as f:
        model = pickle.load(f)

except FileNotFoundError:
    model = None
    print("Position_Salaries.pkl file not found.")

except Exception:
    model = None
    err_type, err_msg, err_line = sys.exc_info()

    print(
        f"Error from line {err_line.tb_lineno} "
        f"due to {err_type.__name__} "
        f"reason was : {err_msg}"
    )


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# Prediction
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        if model is None:
            return render_template(
                "index.html",
                prediction_text="Model Not Loaded."
            )

        level = float(request.form["Level"])

        if level < 1:
            return render_template(
                "index.html",
                prediction_text="Level must be greater than 0."
            )

        sample = np.array([[level]])

        prediction = model.predict(sample)

        if prediction.ndim == 2:
            result = float(prediction[0][0])
        else:
            result = float(prediction[0])

        return render_template(
            "index.html",
            prediction_text=f"₹ {result:,.2f}"
        )

    except ValueError:

        return render_template(
            "index.html",
            prediction_text="Please enter only numeric values."
        )

    except KeyError:

        return render_template(
            "index.html",
            prediction_text="Input field not found."
        )

    except Exception:

        err_type, err_msg, err_line = sys.exc_info()

        print(
            f"Error from line {err_line.tb_lineno} "
            f"due to {err_type.__name__} "
            f"reason was : {err_msg}"
        )

        return render_template(
            "index.html",
            prediction_text=f"Error : {err_msg}"
        )


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)