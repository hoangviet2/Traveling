from typing import Text
from flask import Flask, app,render_template,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from sqlalchemy.sql import func

app = Flask(__name__)
pass_word = 'Hoang Ben'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:'+pass_word+'@localhost/Height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://navmifozkecbyb:7ce65dd30128a312bc62194929f4f32eafa85d117cde7be002d751cda7ad61ab@ec2-3-218-149-60.compute-1.amazonaws.com:5432/d294es058jic8i?sslmode=require'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False
class Data(db.Model):
    __tablename__= "data"
    id = db.Column(db.Integer,primary_key = True)
    emailPre = db.Column(db.String(120),unique = True)
    heightPre = db.Column(db.Integer)
    def __init__(self,emailPre,heightPre):
        self.emailPre = emailPre
        self.heightPre = heightPre

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods = ['POST'])
def success():
    if request.method == 'POST':
        file = request.files["file_name"]
        file.save(secure_filename("Uploaded"+file.filename))
        return render_template("index.html",btn="download.html") 

@app.route("/download")
def download():
    pass
if __name__ == '__main__':
    app.debug = True
    app.run()
