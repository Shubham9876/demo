##############################################
# SYNTAX OF FLASK
##############################################
# from flask import Flask

# app=Flask(__name__)## WSGI app

# @app.route('/')# API ## Default API
# def one():
#     return("API SUCCESS!!!")

# if __name__ =='__main__':
#     app.run()


#############################################3
##############################################
# url for routing
from flask import Flask

app=Flask(__name__)## WSGI app

@app.route('/')# API ## Default API
def one():
    return("API SUCCESS!!!")

@ app.route('/predict')
def prefict():
    return "Predict API"

@ app.route('/app/data')
def data():
    return "app & data API"
if __name__ =='__main__':
    app.run()


#######################################
# app.run(host,port,debug,options)

#       host=default>> 127.0.0.1 (Localhost)
#       port=5000, e.g AWS >> 8080
#       debug= Default False, if set True the porvide debug information on console

######################################
# app.run argument
######################################

# from flask import Flask

# app=Flask(__name__)## WSGI app

# @app.route('/')# API ## Default API
# def one():
#     return("API SUCCESS!!!")

# if __name__ =='__main__':
#     app.run(host='127.0.0.1' ,port=5000, debug=False)

##############################################
###############################################

from flask import Flask

app=Flask(__name__)## WSGI app

@app.route('/')# API ## Default API
def one():
    return("API SUCCESS!!!")

if __name__ =='__main__':
    app.run(host='localhost' ,port=5000, debug=False)