#The API is https://randomuser.me/api which spits out made up users
from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get("https://randomuser.me/api/")


#print(response.status_code)  # Testing; 200 means it is connected
#print(response.json())  # Testing to be sure the JSON returns


@app.route('/')


def get_name():
    first_name = (response.json()['results'][0]['name']['first'])
    #print(first_name) # Testing
    last_name = response.json()['results'][0]['name']['last']
    #print(last_name) # Testing
    # gender = response.json()['results'][0]['gender']
    # print(gender) # Testing
    #age = response.json()['results'][0]['dob']['age']
    #print(age) # Testing
    character_name = first_name, last_name
    # Can add age, gender
    #print(f"Your random character name is: {first_name, last_name}")
    return render_template("index.html", character_name=character_name)


def home():
    #Rendering HTML Elements
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)  # This might be app.run(host="0.0.0.0" or "127.0.0.1", port=80)
