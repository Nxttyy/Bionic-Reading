from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://bionic-reading1.p.rapidapi.com/convert"


payload = {
	"content":"Hello World",
	"response_type":"html",
	"request_type":"html",
	"fixation":"1",
	"saccade":"10"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com",
	"X-RapidAPI-Key": "8d0ff07d7fmshebfc3ce9513926cp1da824jsna77a200e9cdf"
}

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)

@app.route('/')
def home():
    return response.text

if __name__ == '__main__':
    app.run( debug = True )
