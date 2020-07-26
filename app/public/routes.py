from flask import abort, render_template, request
from . import public_bp


@public_bp.route('/',methods=['GET'])
def index():
    return render_template("index.jinja")

@public_bp.route('/enviar',methods=['GET', 'POST'])
def send():
    form_sended = False
    if request.method == 'POST':
        form_sended = True

    return render_template("new.jinja", form_sended = form_sended)

@public_bp.route('/contacto',methods=['GET'])
def contact():
    return render_template("contacto.jinja")

@public_bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.jinja')