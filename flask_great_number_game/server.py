from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = '12l3k1j2l3k1j2l3k1j2l3k1'

@app.route('/')
def index():
  session['computer_num'] = random.randint(1, 100)
  return render_template('index.html')

@app.route('/process_guess', methods=['POST'])
def process_guess():
  print('*******************************')
  print(f"request.form dictionary: {request.form}")
  print(f"User guessed: {request.form['guess']}")
  print(f"Computer number: {session['computer_num']}")
  user_guess = int(request.form['guess'])
  computer_num = int(session['computer_num'])
  if (user_guess > computer_num):
    is_too_high = True
    print('GUESSED TOO HIGH')
  elif (user_guess < computer_num):
    is_too_low = True
    print('GUESSED TOO LOW')
  else:
    is_correct = True
    print('GUESSED JUST RIGHT')
    # Create key value pairs in session for the boolean variables
  return redirect('/results')

@app.route('/results')
def result():
  # check booleans in session
  return render_template('result.html')

if __name__ == '__main__':
  app.run(debug=True)