from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name", validators=[InputRequired(message="Name can't be blank")])
    species = SelectField("Species", choices=[
                          ('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")
