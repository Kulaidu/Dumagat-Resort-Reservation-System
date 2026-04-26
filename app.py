from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/reserve")
def book():
    return render_template("reservation.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/login")
def login():
    return render_template("login.html")

# ADMIN ROUTES ============================================================

@app.route("/dashboard")
def dashboard():
    return render_template("admin/dashboard.html")

@app.route("/reservations")
def reservations():
    return render_template("admin/reservations.html")

@app.route("/add_reservations")
def add_reservations():
    return render_template("admin/add_reservations.html")

@app.route("/profile")
def profile():
    return render_template("admin/profile.html")

if __name__ == "__main__":
    app.run(debug=True)