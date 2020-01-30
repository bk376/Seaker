from flask import render_template, redirect, url_for, flash

from seaker import app, db, bcrypt
from seaker.forms import RegistrationForm, LoginForm
from seaker.models import User

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to login', 'success')
        return redirect(url_for('login'))
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

