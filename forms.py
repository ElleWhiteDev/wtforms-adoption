from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a new pet"""

    name = StringField("Pet Name", validators=[
                       InputRequired("Pet name cannot be blank")])
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )
    age = FloatField("Pet Age", validators=[Optional(), NumberRange(
        min=0, max=30, message="Age must be a number 0 - 30 ")])
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Please enter a valid URL")])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Currently available for adoption?")


class EditPetForm(FlaskForm):
    """Form to edit existing pet data"""

    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Please enter a valid URL")])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Currently available for adoption?")
