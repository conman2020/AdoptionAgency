from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, NumberRange, URL, Length




class AddPetForm(FlaskForm):
    name=StringField("Pet name", validators=[InputRequired(message="Name cannot be blank")])
    species=StringField("Species name", validators=[InputRequired(message="Species cannot be blank")])
    photo_url= StringField("Photo URL")
    age= IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)],)
    notes= StringField("Notes")
    available = BooleanField("Available or Not")



class EditPetForm(FlaskForm):
    photo_url= StringField("Photo URL", validators=[Optional(), URL()],)
    notes = StringField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )
    available = BooleanField("Available?")