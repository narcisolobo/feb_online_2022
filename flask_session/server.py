from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
  session['first_name'] = request.form['first_name']
  return redirect('/result')

@app.route('/result')
def result():
  first_name = session['first_name']
  return render_template('result.html', first_name = first_name)

if __name__ == '__main__':
  app.run(debug=True)