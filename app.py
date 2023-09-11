import flask
from flask import Flask,render_template,request
import requests

app = Flask(__name__)

#make a route and render all the html templates in this route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')

        #take a variable to show the json data
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=81ca69f89181e36a0c4c80ae52529497')

        #read the json object
        json_object = r.json()

        #take some attributes like temperature,humidity,pressure of this 
        temperature = float(json_object['main']['temp']-273.15) #this temparetuure in kelvin
        humidity = float(json_object['main']['humidity'])
        pressure = float(json_object['main']['pressure'])
        wind = float(json_object['wind']['speed'])

        #atlast just pass the variables
        
        return render_template('home.html',temperature=temperature,pressure=pressure,humidity=humidity,city_name=city_name,wind=wind)
    else:
        return render_template('home.html') 


if __name__ == '__main__':
    app.run(debug=True)