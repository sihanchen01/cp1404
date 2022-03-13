from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_word():
    return "<h1>Hello World!</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "<h1>Hello {}</h1>".format(name)


def celsius_to_fahrenheit(celsius: str) -> str:
    """convert celsius value to fahrenheit value"""
    return str(float(celsius) * 1.8 + 32)


@app.route('/f/<celsius>')
def fahrenheit(celsius: float):
    return f"<h1>Celsius: {celsius}&#8451 is Fahrenheit: {celsius_to_fahrenheit(celsius)}&#8457</h1>"


if __name__ == "__main__":
    app.run(debug=True)
