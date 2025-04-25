from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/media_km', methods=['POST'])
def media_km ():
    distancia = float(request.form['distancia'])
    velocidade = float(request.form['velocidade'])
    media = round(distancia / velocidade, 2)
    tempo= str(timedelta(hours=media))

    return render_template('index.html', media=tempo)

if __name__ == '__main__':
    app.run(debug=True)