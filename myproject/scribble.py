from flask import Flask

app = Flask(__name__)

@app.route('/<int:number>')
def square(number):
    return str(number ** 2)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

    
