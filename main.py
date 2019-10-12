from flask import Flask, request, render_template 
from flask import redirect, send_from_directory

app = Flask(__name__,
                static_url_path='',
                static_folder='statics',
                template_folder='templates')

app.config.from_pyfile('settings.cfg')    

@app.route('/',methods=['GET', 'POST'])
def root():
    form_sended = False
    if request.method == 'POST':
        form_sended = True

    return render_template("index.jinja", form_sended = form_sended)

@app.route('/admin',methods=['GET'])
def admin():
    return render_template("admin.jinja")

if __name__ == '__main__':
        app.run()

