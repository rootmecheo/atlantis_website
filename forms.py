from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# create job form
class JobForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  location = StringField('Location', validators=[DataRequired()])
  salary = StringField('Salary')
  currency = StringField('Currency', validators=[DataRequired()])
  responsibilities = TextAreaField('Responsibilities', validators=[DataRequired()])
  requirements = TextAreaField('Requirements', validators=[DataRequired()])

# create application form

# create profile form

# create login form

# create register form

# create contact form