import os

from flask import Flask

app = Flask(__name__)
count = 0
@app.route('/')
def hello_world():
    return 'Hello ace girl'

@app.route('/count')
def count_test():
    count = count + 1
    return f"Hello ace girl, {count}"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
