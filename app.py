from flask import Flask, render_template
import requests

app = Flask(__name__)

location = {
   'name': 'Des Moines, IA' ,
   'temp': '45'
}
url = 'http://api.openweathermap.org/data/2.5/weather?q={Des Moines, ia}&APPID=af95d952bd6aa6b90196955ed9c43cb9?'
response = requests.get(url)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',location=location, response=response)

if __name__ == "__main__":
    pass