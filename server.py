from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "thisIsSecret"


@app.route("/")
def index():

    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1


    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1

    return render_template("index.html")

@app.route("/add_2")
def add_2():

    session['count'] += 1

    return redirect("/")


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


@app.route("/process", methods=['POST'])
def process():
    # print(request.form['number'])

    session['count'] += int(request.form['number']) -1

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
