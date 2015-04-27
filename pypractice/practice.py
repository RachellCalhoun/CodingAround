from flask import Flask, render_template
app = Flask(__name__)


@app.route("/<name>")
def name_page(name):
    return render_template('practice.html')

@app.route("/")
def home():
    return render_template('practice.html')

if __name__ == "__main__":
    app.run(debug=True)
