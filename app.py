from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')
@app.route("/listings")
def index_page():
      return render_template('index.html')

print(__name__)
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)