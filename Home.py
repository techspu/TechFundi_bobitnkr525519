from flask import Flask, render_template, url_for, flash, redirect
from Forms import RegistrationForm, loginForm
app = Flask(__name__,template_folder='Templates')

app.config['SECRET_KEY'] = '3f6c7d29c5d0419b8f37dc27539ce891'

posts = [
    {
        'author': 'karuga ken',
        'title': 'Patient Zero',
        'content': 'covid-19 ',
        'date_posted': 'July 27, 2020',
    },
    {
        'author': 'Elizabeth nungari',
        'title': 'first contact with Patient Zero',
        'content': 'location: Nairobi',
        'date_posted': 'July 29, 2020',
    }


]

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    flash('YOU HAVE SUCCESSFULLY LOGGED IN', 'success')
    return render_template("Home.html", posts=posts)


@app.route("/About")
def page():
    return render_template("About.html", title='About')


@app.route("/Register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("login.html", title='login', form=form)


if __name__ == '__main__':

    app.run(debug=True)
