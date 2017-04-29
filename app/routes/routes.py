from flask import redirect, render_template, url_for
from app import app
from app.controllers.beer_controller import BeerController

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    beers = BeerController.search()
    return render_template('home.html.j2', beers=beers)
