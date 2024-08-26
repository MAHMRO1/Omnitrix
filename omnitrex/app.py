from cs50 import SQL
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

# Configure application
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///omnitrex.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

@app.route("/submit", methods=["GET", "POST"])
def favorite():
    if request.method == "POST":
        name = request.form.get("username")
        alien = request.form.get("alien")

        # Ensure name and alien were entered
        if not name:
            return apology("must provide name", 400)
        elif not alien:
            return apology("must choose an alien", 400)
        
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", name)
        if existing_user:
            return apology("username already exists", 400)

        # Insert the new user into the database
        db.execute("INSERT INTO users (username, alien) VALUES (?, ?)", name, alien)
    
    # Fetch all submissions from the database
    submissions = db.execute("SELECT username, alien FROM users")
    return render_template("favorite.html", submissions=submissions)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/diamondhead")
def diamondhead():
    return render_template("diamondhead.html")

@app.route("/fourarms")
def fourarms():
    return render_template("fourarms.html")

@app.route("/heatblast")
def heatblast():
    return render_template("heatblast.html")

@app.route("/xlr8")
def xlr8():
    return render_template("xlr8.html")

@app.route("/upgrade")
def upgrade():
    return render_template("upgrade.html")

@app.route("/ghostfreak")
def ghostfreak():
    return render_template("ghostfreak.html")

@app.route("/ripjaws")
def ripjaws():
    return render_template("ripjaws.html")

@app.route("/stinkfly")
def stinkfly():
    return render_template("stinkfly.html")

@app.route("/greymatter")
def greymatter():
    return render_template("greymatter.html")

@app.route("/wp")
def wp():
    return render_template("wp.html")


