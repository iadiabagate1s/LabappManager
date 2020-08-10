from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,IntegerField,TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo



class LoginForm(FlaskForm):
    """Login form."""

    last_name = StringField('Enter last Name', validators=[DataRequired()])
    lab_id = PasswordField('Enter Lab Id', validators= [DataRequired()])
    
    
class Register(FlaskForm):
    """Form for adding users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    lab_id = PasswordField('create a lab id', validators=[InputRequired()])
    avatar = StringField('Enter a image Url')
    

class Edituser(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    avatar = StringField('Enter a image Url')
    admin = BooleanField('Make User Admin')
    
class Projform(FlaskForm):
    """Form for adding users."""
    quote_id = IntegerField('Quote Id', validators= [DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    sample_type= StringField('Sample Type', validators=[DataRequired()])
    num_samples = IntegerField('Number of Samples', validators=[DataRequired()])
    process1= TextAreaField('Enter Process', validators=[InputRequired()])
    freezer = SelectField('Location: Freezer', validators=[DataRequired()])
    
    
class Tasksform(FlaskForm):
    
    quote_id = SelectField(' Select a Project', coerce = int)
    lab_id = SelectField('Select a Technitian' )
    Kit = StringField('Process')
    task = TextAreaField('Task')