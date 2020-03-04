from flask import Flask
import os
import sys

app = Flask(__name__)

@app.route('/invoke', methods=['GET','POST'])
def hello_world():
    return sys.version

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("FC_SERVER_PORT", "9000"))