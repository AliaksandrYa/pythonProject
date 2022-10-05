from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # передача в функцию
def index():
    return render_template('index.html', name='My Name',
                           project_number=100, title='HOME PAGE')

