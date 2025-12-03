import os

from flask import Flask, flash, redirect, render_template, request

from tasks import add

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "super-secret")


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/add", methods=["POST"])
def add_inputs():
    try:
        x = int(request.form["x"])
        y = int(request.form["y"])
        result = add.delay(x, y)
        flash(f"Job submitted! Task ID: {result.id[:8]}...")
    except (ValueError, KeyError):
        flash("Please enter valid numbers for both X and Y.")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
