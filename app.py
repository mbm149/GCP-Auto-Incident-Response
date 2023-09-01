from flask import Flask, render_template, request, redirect, url_for
import requests 


app = Flask(__name__)

@app.get('/')
def index():  
    return render_template('index.html')



@app.route('/results', methods = ['POST'])
def results():

    api_k = "c3e372f796f5a343511f0b56ac9201a0"

    if request.method == 'POST':
        user_input = request.form['form_todo']
        data_ = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&APPID={api_k}")

        if data_.json()['cod'] == '404':
            return 'No City found! <p> <br/> <a href="/">Back Home</a>'
        else:
            descripton = data_.json()['weather'][0]['description']
            weather = data_.json()['weather'][0]['main']
            temp = data_.json()['main']['temp']
            feels_like = data_.json()['main']['feels_like']
            humidity = data_.json()['main']['humidity']

            return 'City  %s  <p> Temperatur:  %s  <p> Feels Like: %s <p>  Description:  %s  <p> Weather:  %s  <p>  Humidity:  %s  </p> <br/> <a href="/">Back Home</a>' % (user_input, temp, feels_like, descripton, weather, humidity)
    return '#############  <p> <br/> <a href="/">Back Home</a>'


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)

