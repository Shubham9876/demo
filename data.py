from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('one.html')

@app.route('/userdata',methods=['GET','POST'])
def data():
    var=request.form
    print(var)
    return "SUCCESS"

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)