from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>HI Sri This is Flask Application Running from CICD plz check once!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
