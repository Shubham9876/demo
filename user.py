from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def index():
    return "API Point"

@app.route('/admin/<user_data>')
def admin(user_data):
    return 'Welcome admin '+user_data
    

@app.route('/guest/<user_data>')
def guest(user_data):
    return 'Welcome guest '+user_data
 

@app.route('/user_data/<name>')
def user_data(name):
     if name=='admin':
         user='admin'
     else:
         user='guest'
    
     return redirect(url_for(user,user_data=name))



if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)