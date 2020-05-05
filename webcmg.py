from flask import Flask
from flask import render_template, redirect, request, flash, request
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_mail import Mail, Message

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '7d441d27d441f27785d441f2b6166a'

class ReusableForm(FlaskForm):
    fname = TextField('fName:', validators=[DataRequired()])
    lname = TextField('lName:', validators=[DataRequired()])
    email = TextField('Email:', validators=[DataRequired(), validators.Length(min=6, max=35)])
    message  = TextField('mesg:')

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)

mail = Mail()

app.config["MAIL_SERVER"] = "smtp.office365.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = 'info@webcmg.com'
app.config["MAIL_PASSWORD"] = '120+Skipper'
 
mail.init_app(app)
     
@app.route('/')
def home():
    return render_template('home.html',
                          title="WebCMG",
                          description="Website creation, management & growth services",
                          author="WEbCMG, Inc., Los Gatos, CA, USA")

@app.route('/about')
def about():
    return render_template('about.html',
                          title="WebCMG",
                          description="Website creation, management & growth services",
                          author="WEbCMG, Inc., Los Gatos, CA, USA")


@app.route('/experts_dir/<expert>', methods=["GET", "POST"])
def experts(expert):
    return render_template('experts_dir.html',
                          expert=expert,
                          title="WebCMG",
                          description="Website creation, management & growth services",
                          author="WEbCMG, Inc., Los Gatos, CA, USA")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ReusableForm(request.form)
  
 
  if request.method == 'POST':
      fname=request.form['fname']
      lname=request.form['lname']
      email=request.form['email']
      message =request.form['message']
      if form.validate_on_submit():
        msg = Message("new customer query", sender='info@webcmg.com', recipients=['info@webcmg.com'])
        msg.body = """
        From: %s %s <%s>
        %s
        """ % (form.fname.data, form.lname.data, form.email.data, form.message.data)
        mail.send(msg)
        return render_template('contact.html',success=True)
      else:
        flash('Error: All the form fields are required. ')
  

  return render_template('contact.html', 
                            form=form,
                            title="WebCMG",
                            description="Website creation, management & growth services",
                            author="WEbCMG, Inc., Los Gatos, CA, USA")

  
if __name__ == "__main__":
    app.run(host='0.0.0.0')
