from flask import Flask, render_template, url_for, flash, redirect
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


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="ben@local.com" and form.password.data=="password":
            flash('You have been logged in', 'success')
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
