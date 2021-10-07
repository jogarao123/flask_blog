import re
from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user_page(name):
    return render_template('user.html',username=name)

@app.errorhandler(404)
def page_not_found(e):
    return "not fud"
@app.errorhandler(500)
def internal_server(e):
    return "internal server"


if __name__=='__main__':
    app.run(debug=True)
