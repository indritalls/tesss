from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/mulai", methods=['POST', 'GET'])
def truth():
	if (request.form['name_input']=="truth"):
		flash("cobalah jujur")
		return render_template("index.html")

	if (request.form['name_input']=="dare"):
		flash("beranilah menerima tantangan ini")
		return render_template("index.html")
