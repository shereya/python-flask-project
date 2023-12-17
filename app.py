from flask import Flask
app = Flask(__name__)
@app.route("/")
def functionhello():
  return "<h1>Hello Shereya</h1>"
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
