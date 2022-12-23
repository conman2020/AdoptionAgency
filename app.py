from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)



@app.route('/')
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/<int:department_id>")
def show_pet(department_id):
    """Show info on a single pet."""

    pet = Pet.query.get_or_404(department_id)
    return render_template("details.html", pet=pet)


@app.route("/add/addpet", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""
    print(request.form)
    form = AddPetForm()
    # raise

    if form.validate_on_submit():
        print(form.name.data)
        print(form.species.data)
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes=form.notes.data
        available=form.available.data
        newpet= Pet(name=name,species=species, photo_url=photo_url, age=age,notes=notes,available=available)
        db.session.add(newpet)
        db.session.commit()
        flash(f"Added {name} to the adoption registry")
        return redirect("/")

    else:
        return render_template(
            "/add/addpet.html", form=form)




@app.route('/edit/<int:department_id>/editpet', methods=["GET", "POST"])
def users_updated(department_id):
    """Show edit form for pet."""

    pet = Pet.query.get_or_404(department_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/')

    else:
        # failed; re-present form for editing
        return render_template("/edit/<int:department_id>/pet_edit_form.html", form=form, pet=pet)