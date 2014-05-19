from wtforms import Form, BooleanField, TextField, PasswordField, validators

class Validation(Form):
	result = BooleanField('Shrimp', default = False)
	result1 = BooleanField('Nuts', default = False)
	result2 = BooleanField('Dairy', default = False)
  