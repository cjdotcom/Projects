from flask import Flask, render_template, request
import scraping

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clima', methods=["GET"])
def clima():
    city = request.args.get('city')
    cidade = scraping.cidade(city)
    temp = scraping.temperatura(city)
    respose = f'<h2>{cidade}</h2><h1 style="color:red">{temp}C</h1>'

    return respose

if __name__ == '__main__':
    app.run(debug=True)
