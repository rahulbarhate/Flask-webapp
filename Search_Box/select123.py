import os,sys
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


actor = []
objec = []
emotion = []
frame_no = []
 
# App config.
DEBUG = True
app = Flask(__name__)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


#class ReusableForm(Form):
#    name = TextField('Name:', validators=[validators.required()])

@app.route("/")    
def index():
    return render_template('select123.html')
 
@app.route('/select123', methods=['GET','POST'])
def select123():
    #form = ReusableForm(request.form)
    #print(form.errors)
    name=[]
    name=request.form['query']
    print(name)
    return render_template('complete.html')
 
    
 
if __name__ == "__main__":
    app.run(debug = True)
