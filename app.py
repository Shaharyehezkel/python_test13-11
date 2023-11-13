# flask_app.py
from flask import Flask, request, render_template
from comp import sumofdigits, ispal
from col import myzip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_numbers():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2
    return render_template('result.html', result=result)

@app.route('/subtract', methods=['POST'])
def subtract_numbers():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 - num2
    return render_template('result.html', result=result)

@app.route('/sumofdigits', methods=['POST'])
def calculate_sum_of_digits():
    number = int(request.form['number'])
    result = sumofdigits(number)
    return render_template('result.html', result=result)

@app.route('/ispalindrome', methods=['POST'])
def check_palindrome():
    number = str(request.form['number'])
    result = ispal(number)
    return render_template('result.html', result=result)

# @app.route('/myzip', methods=['POST'])
# def custom_zip():
#     it1 = request.form['it1'].split(',')
#     it2 = request.form['it2'].split(',')
#     result = list(myzip(it1, it2))
#     return render_template('result.html', result=result)

@app.route('/myzip', methods=['POST'])
def custom_zip():
    it1 = request.form['it1'].split(',')
    it2 = request.form['it2'].split(',')
    result = list(myzip(it1, it2))

    # Format the result as a string
    result_str = ', '.join(map(str, result))

    return render_template('zip_result.html', result=result_str)

if __name__ == '__main__':
    app.run(debug=True)
