from flask import Flask, render_template, abort
from datetime import datetime
from model import db
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template(
        "test.html",
    message="here is a message from view")

@app.route('/cards/<int:index>')
def cards_view(index):
    try:
        cards =db[index]
        return render_template("cards.html", cards=cards, index=index)
    except IndexError:
        abort(400)



@app.route('/production')
def production():
    return 'this is our production house'

@app.route('/count')
def count():
    global counter
    counter=0
    counter+=1
    return 'the page was served '  + str(counter)+ " times"

@app.route('/date')
def date():
    return 'the page was served at '  + str(datetime.now())



if __name__ =='__main__':
   app.run(debug=True, port=5000)
