from flask import Flask, request, render_template 
from flask import redirect, send_from_directory

app = Flask(__name__,
                static_url_path='',
                static_folder='statics',
                template_folder='templates')

app.config.from_pyfile('settings.cfg')    

@app.route('/',methods=['GET'])
def index():
    return render_template("index.jinja")

@app.route('/send',methods=['GET', 'POST'])
def send():
    form_sended = False
    if request.method == 'POST':
        form_sended = True

    return render_template("new.jinja", form_sended = form_sended)

@app.route('/admin',methods=['GET', 'POST'])
def admin():
    return render_template("admin.jinja")

if __name__ == '__main__':
        app.run()

