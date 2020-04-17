from flask import Flask
from flask import render_template, redirect

app = Flask(__name__, template_folder="templates")


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

@app.route('/contact')
def contact():
    return render_template('contact.html',
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

 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
