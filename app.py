from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234567890@localhost/lujainaswebapp'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pqzidtylsmhgvf:f73003e618aa52414ec8808dc8add0c6303839b06510a5acade1b4b03d468252@ec2-44-206-214-233.compute-1.amazonaws.com:5432/d8lhrd1g4ce9b'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    location = db.Column(db.String(200))
    license = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, location, license, rating, comments):
        self.customer = customer
        self.location = location
        self.license = license
        self.rating = rating 
        self.comments = comments
    


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        location = request.form['location']
        license = request.form['license']
        rating = request.form['rating']
        comments = request.form['comments']

        if customer=='':
            return render_template('index.html', message="Please make sure to enter your name")
        
        data = Feedback(customer, location, license, rating, comments)
        db.session.add(data)
        db.session.commit()
        send_mail(customer, location, license, rating, comments)
        return render_template('success.html')
        
        
if __name__ == '__main__':
    app.run()
