from flask import Flask, request, render_template
import cesar

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cifrar', methods=["GET"])
def cifrar():
    palavra = request.args.get('frase').upper()
    key = request.args.get('salto')
    if key == '':
        response = cesar.cifrar(str(palavra), 0)
    else:
        response = cesar.cifrar(str(palavra), int(key))
    
    return f'<h1 style="text-align: center;">{response}</h1>'

@app.route('/decifrar', methods=["GET"])
def decifrar():
    palavra = request.args.get('frase').upper()
    key = request.args.get('salto')
    if key == '':
        response = cesar.decifrar(str(palavra), 0)
    else:
        response = cesar.decifrar(str(palavra), int(key))

    return f'<h1 style="text-align: center;">{response}</h1>'

if __name__=='__main__':
    app.run(debug=True)