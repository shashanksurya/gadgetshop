from app import app
from flask import Flask
from flask import session
from flask import request
from flask import render_template

# remove before production
app.config.update(dict(DEBUG=True))
#change before production
app.secret_key = 'my_re@lly_secr3tkey' #which is not really a great secret

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)