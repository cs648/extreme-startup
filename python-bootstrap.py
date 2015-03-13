from flask import Flask, request
import answer
import re

app = Flask(__name__)

pathways = [
    (),
    (r'[^:]*: Convert (\d+) into Roman Numerals', [1], answer.write_roman)
]

@app.route('/')
def hello_world():
    try:
        question = request.args.get('q')
        for path in pathways:
            match = re.search(path[0],question)
            if match:
                return path[2](match.group(path[1]))
        else:
            print question
        return ""
    except:
        return ""


if __name__ == '__main__':
    app.run(debug=True, port=1337, host="0.0.0.0")
