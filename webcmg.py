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

# @app.route('/layout/<dest>', methods=["GET", "POST"])
# def layout(dest):
#    return render_template('layout.html',
#                           title=dest,
#                           dest=dest,
#                          description="Travel blogs, tips and advice for " + dest)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
