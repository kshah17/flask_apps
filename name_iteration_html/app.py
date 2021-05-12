from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route("/list")
def _list():
    list_1 = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template("list.html", users=list_1)


if __name__ == "__main__":
    app.run(debug=True)
