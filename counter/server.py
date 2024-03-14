from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "1234-abcd"


@app.route("/")
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1

    return render_template("index.html", counter=session["counter"])


@app.post("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
