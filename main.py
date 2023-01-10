from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'hello world!'

app.run(host='0.0.0.0')