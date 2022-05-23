from flask import Flask, render_template
import requests
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

url = "https://bionic-reading1.p.rapidapi.com/convert"



headers = {
	"content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com",
	"X-RapidAPI-Key": "8d0ff07d7fmshebfc3ce9513926cp1da824jsna77a200e9cdf"
}

#response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)

@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        payload = {
            "content":str(form.data.data),
            "response_type":"html",
            "request_type":"html",
            "fixation":"1",
            "saccade":"10"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return render_template('response.html', title='Response', data=response.text)
    return render_template('Home.html', title='Home', form=form)

if __name__ == '__main__':
    app.run( debug = True )
