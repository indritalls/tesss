from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("Pilihlah Truth or Dare")
	return render_template("index.html")

@app.route("/mulai", methods=['POST', 'GET'])
def truth():
	flash("cobalah untuk jujur")
	return render_template("index.html")
