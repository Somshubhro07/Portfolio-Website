from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models.database import db, connect_db
from flask import Flask, render_template, request, redirect, url_for
from models.models import Leaderboard, db, connect_db, Project, Contact 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:somshubhro@localhost/portfolio_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

connect_db(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/passions')
def passions():
    return render_template('passions.html')


@app.route('/portfolio')
def portfolio():
    # Query all projects from the database
    projects = Project.query.all()
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a new contact entry in the database
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        # Redirect to thank you page or show success message
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route("/game")
def game():
    return render_template("game.html")

# Route for posting scores
@app.route("/submit_score", methods=["POST"])
def submit_score():
    score = request.form["score"]
    new_score = Leaderboard(score=score)
    db.session.add(new_score)
    db.session.commit()
    return redirect("/game")

# Route for getting the leaderboard
@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    top_scores = Leaderboard.query.order_by(Leaderboard.score.desc()).limit(5).all()
    return jsonify([{"score": score.score} for score in top_scores])


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
