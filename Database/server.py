from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/add', methods= ['POST'])
def addData():
    content = request.json
    print(content)
    return "Success"


if __name__ == '__main__':
    app.run(port=5001)