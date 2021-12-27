from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/tes")
def index():
	flash("Ketikkan truth atau dare")
	return render_template("index.html")

@app.route("/truth", methods=['POST', 'GET'])
def handle_message(message):
	if (message=="truth"):
		flash("Coba jujur")
		return render_template("index.html")
