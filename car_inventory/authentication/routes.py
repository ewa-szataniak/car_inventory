from flask import Blueprint, render_template, request, redirect, url_for
from ..forms import UserLoginForm
from ..models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    userform = UserLoginForm()

   

    if request.method == 'POST' and userform.validate_on_submit():
            email = userform.email.data
            username = userform.username.data
            password = userform.password.data
            print(email, password)

            user = User(email, password)

            db.session.add(user)
            db.session.commit()

            print('User created')
            return redirect(url_for('auth.signin'))
        
    return render_template('signup.html', userform=userform)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    userform = UserLoginForm()

    try:
        if request.method == "POST" and userform.validate_on_submit():
            email = userform.email.data
            password = userform.password.data
            logged_user = User.query.filter(User.email == email).first()
            print(email, password)

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                print('Validated')
                login_user(logged_user)
                return redirect(url_for('site.home'))
                
            else:
                print('Password incorrect')
                return redirect(url_for('auth.signin'))
        
    except:
        raise Exception('Invalid Form Data: Please Check Your Form')
    return render_template('signup.html', userform=userform)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    print('You are sign out')
    return redirect(url_for('site.home'))

    

