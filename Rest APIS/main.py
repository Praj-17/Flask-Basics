from flask import Flask,jsonify
def sum(a, b):
    return a+b
def avg(a, b):
    return sum(a, b)/2

def is_even(a):
    return True if a%2 ==0 else False

app = Flask(__name__)

@app.route('/even/<int:n1>/<int:n2>')
def main(n1, n2):
    result = { 'status': is_even(n1),
              'number': n1,
              'statu2': avg(n1, n2)
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug= True)