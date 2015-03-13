from flask import Flask, request
import answer
import re

app = Flask(__name__)

pathways = [
    (r'[^:]*: Convert (\d+) into Roman Numerals', [1], answer.write_roman),
    (r'[^:]*: which of the following numbers is the largest: (.*)', [1], answer.largest),
    (r'[^:]*: what is the (\d+).. number in the Fibonacci sequence', [1], answer.fib)
    (r'[^:]*: what is (\d) multiplied by (\d)', [1,2], answer.multiply)
]

@app.route('/')
def hello_world():
    question = request.args.get('q')
    try:
        for path in pathways:
            match = re.search(path[0],question)
            if match:
                ans = path[2](*[match.group(i) for i in path[1]])
                print "Answered:", question, "with", ans
                return ans
        else:
            print question
        ans = answer.answer(question)
        print "Answered:", question, "with", ans
        return ans
    except Exception as e:
        print "Question:", question
        print "Exception", e
        return ""


if __name__ == '__main__':
    app.run(debug=True, port=1337, host="0.0.0.0")
