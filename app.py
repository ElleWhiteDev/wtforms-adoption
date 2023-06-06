from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import *
from forms import *

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    """List of all pets"""
    
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET","POST"])
def add_new_pet():
    """New pet form"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data.capitalize()
        species = form.species.data.capitalize()
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data.capitalize()

        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes,available=True)
        db.session.add(pet)
        db.session.commit()

        flash(f"{name} the {species} has been added!", "success")
        return redirect("/")
    else:
        return render_template("new_pet_form.html", form=form)
    

@app.route("/<int:id>", methods=["GET","POST"])
def pet_detail(id):
    """Display/edit pet details"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash("Edit saved successfully", "succcess")
        return render_template("edit_pet.html", pet=pet, form=form)
    else:
        print(form.errors)
        return render_template("edit_pet.html", pet=pet, form=form)
