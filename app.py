from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, j4EmailAddress
from flask_wtf import CSRFProtect

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = ""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app,db)
app.secret_key = ''
csrf = CSRFProtect(app)

@app.route('/', methods=["POST", "GET"])
def index():

    j4EmailSubmissionMessage = ""

    if request.method == "POST":
        try:
            email = request.form['j4Email']
            if "@" in email:
                new_email = j4EmailAddress(email=email)
                db.session.add(new_email)
                db.session.commit()
                j4EmailSubmissionMessage = "Thanks for showing your interest, please keep an eye on your emails for our release"
            else:
                j4EmailSubmissionMessage = "You must enter an email"
        except:
            j4EmailSubmissionMessage = "Something went wrong, please make sure you enter your email address correct and have not signed up already"

    return render_template('index.html', j4EmailSubmissionMessage = j4EmailSubmissionMessage)