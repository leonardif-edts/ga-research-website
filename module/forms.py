from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
	count = IntegerField('Count', default=1, validators=[DataRequired()])
	submit = SubmitField('Buy')