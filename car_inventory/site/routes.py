
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from car_inventory.forms import CarForm
from car_inventory.models import Car, db 
from car_inventory.helpers import random_joke_generator


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print('Car project is here!')
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    carform = CarForm()

    try:
        
        if request.method == 'POST' and carform.validate_on_submit():
            make = carform.make.data
            model = carform.model.data
            price = carform.price.data
            year = carform.year.data
            is_new = carform.is_new.data
            if is_new == 'yes':
                is_new = True
            else:
                is_new = False
            vehicle_type = carform.vehicle_type.data
            if carform.dad_joke.data:
                random_joke = carform.dad_joke.data
            else:
                random_joke = random_joke_generator()
            user_token = current_user.token 

            car = Car (make, model, price, year, is_new, vehicle_type, random_joke, user_token)
            
            db.session.add(car)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Car not created, please check your form and try again.')
    
    user_token = current_user.token 
    cars = Car.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=carform, cars=cars )