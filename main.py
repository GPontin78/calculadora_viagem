from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/media_km', methods=['POST'])
def media_km ():
    distancia = float(request.form['distancia'])
    velocidade = float(request.form['velocidade'])

    media = distancia/velocidade

    return render_template('index.html', media=media)

if __name__ == '__main__':
    app.run(debug=True)