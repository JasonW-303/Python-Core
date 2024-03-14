from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play")
def three_nice():
    num = 3
    color = "lightblue"
    return render_template("index.html", num=num, color=color)


@app.route("/play/<int:num>")
def squares_mult(num):
    color = "lightblue"
    return render_template(f"index.html", num=num, color=color)


@app.route("/play/<int:num>/<color>")
def squares_mult_color(num, color):
    return render_template(f"index.html", num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
