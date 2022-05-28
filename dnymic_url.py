
from flask import Flask

my_app=Flask(__name__)
@my_app.route('/')
def one():
    return "API"

@my_app.route('/admin/<name>')
def admin(name):
    return "API"+name

@my_app.route('/value/<no>')
def value(no):
    return "API="+no

@my_app.route('/value1/<int:no>')
def value1(no):
    return "API="+str(no)

if __name__ =='__main__':
    my_app.run(host='127.0.0.1',port=5000,debug=True)


###################Basic web app/flask app is ready to use