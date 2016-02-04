from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField, PasswordField, StringField, SelectField
from wtforms.validators import DataRequired, EqualTo


class ChatLogin(Form):
    userName = StringField('Username', validators=[DataRequired()])
    userPassword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ChatRegistration(Form):
    userName = StringField('Username', validators=[DataRequired()])
    userPassword = PasswordField('Password', validators=[DataRequired()])
    userPasswordConfirm = PasswordField('Confirm Password', validators=[EqualTo('userPassword')])
    submit = SubmitField('Submit')


class Search(Form):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddItem(Form):
    itemName = StringField('Item Name', validators=[DataRequired()])
    itemDescription = TextAreaField('Item Description', validators=[DataRequired()])
    itemImage = StringField('Item Image URL')
    itemShop = SelectField('Item Shop',
                           choices=[('1', 'Fire Magic'), ('2', 'Water Magic'), ('3', 'Earth Magic'), ('4', 'Air Magic'),
                                    ('5', 'General Magic'), ('6', 'Healing Magic'), ('7', 'Holy Magic'),
                                    ('8', 'Ice Magic'), ('9', 'Light/Dark Magic'), ('10', 'Mind Magic'),
                                    ('11', 'Nature Magic'), ('12', 'Unholy Magic')])
    submit = SubmitField('Submit')


class TweetForm(Form):
    tweet_text = TextAreaField('Write your tweet here.', validators=[DataRequired()])
    submit = SubmitField('Submit')
