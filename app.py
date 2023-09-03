from flask import Flask, render_template, request, redirect, url_for
import requests 


app = Flask(__name__)

@app.route('/' ,methods = ['GET','POST'])
def index():


    if request.method == 'POST':
        city = request.form['form_city']
        return  redirect(url_for("city", usr=city))
    else:
        return  render_template('index.html')


@app.route("/<usr>")
def city(usr):
    api_k = "c3e372f796f5a343511f0b56ac9201a0"
    data_ = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={usr}&APPID={api_k}")

    if data_.json()['cod'] == '404':
        return 'No City found! <p> <br/> <a href="/">Back Home</a>'
    #else:
    else:
        descripton = data_.json()['weather'][0]['description']
        weather = data_.json()['weather'][0]['main']
        temp = data_.json()['main']['temp']
        feels_like = data_.json()['main']['feels_like']
        humidity = data_.json()['main']['humidity']

        return  f"<h1> {usr} </h1>  <p> Temperature : {temp} F </p> <p> Weather : {weather} </p>  <p> Description : {descripton} </p> <p> Humidity : {humidity} </p> <p> Feels like : {feels_like} </p>  <p> <br/> <a href="'/'">Back Home</a> </p>" 


if __name__ == '__main__':
    app.run(debug=True)

