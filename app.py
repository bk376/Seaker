from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '63362f584ff66d1bda0281f6520bc914'

posts = [
    {
        'author': 'Ben',
        'title': 'The design journey',
        'content': 'This is  the initial stages of the ultimate blog',
        'date_posted': 'January 20,  2020'
    },
    {
        'author': 'Light Switch',
        'title': 'The other post in design journey',
        'content': 'This is  the initial stages of the ultimate blog and flask power',
        'date_posted': 'January 20,  2020'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
