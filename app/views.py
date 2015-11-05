from app import app
from flask import Flask
from flask import session
from flask import request
from flask import render_template


@app.errorhandler(404)
def pageNotFound(error):
    return "404:page not found"

@app.errorhandler(500)
def badReqest(error):
    return "500:Bad Request"

@app.route('/welcome', methods=('GET', 'POST'))
def welcome():
	title = "High Tech Gadget Shop"
	message = "Welcome to Gadget Shop"
	para = 'Welcome to The Gadget Shop! If you hang around in the Gadget Shop\
	you will find a plethora of cool new gadgets. By staying abreat of new \
	technology we are always brining you gadgets and gizmos that make the \
	world say "wow"'
	return render_template("welcome.html",title=title,message=message\
		,paragraph = para)