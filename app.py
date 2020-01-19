from flask import Flask, render_template

app = Flask(__name__)

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
def hello_world():
    return render_template('home.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
