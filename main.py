from flask import Flask, request, render_template 
from flask import redirect, send_from_directory

app = Flask(__name__,
                static_url_path='',
                static_folder='statics',
                template_folder='templates')

app.config.from_pyfile('settings.cfg')    

@app.route('/',methods=['GET'])
def root():
    return render_template("index.jinja")

@app.route('/admin',methods=['GET'])
def admin():
    return render_template("admin.jinja")

