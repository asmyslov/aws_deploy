from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("checkerboard.html", num = int(8), num2=int(8))

@app.route('/<x>')
def ten_by_ten(x):
    return render_template("checkerboard.html", num = int(x), num2=int(x))


@app.route('/<x>/<y>')
def ten_by_anynumb(x,y):
    return render_template("checkerboard.html", num = int(x), num2 = int(y))


if __name__=="__main__":
    app.run(debug=True)    