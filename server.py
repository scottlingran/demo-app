import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/fetch')
def fetch():
	# Get parameters in URL
	val = request.args.get("val")
	
	# class.dothing(ip)
	data = {
		"a": 1,
		"val": val
	}

	# Convert data to JSON
	response = jsonify(data)

	return (response, 200)

if __name__ == '__main__':
    # app.debug=True
    app.run(host="0.0.0.0", port=8000, threaded=True)
