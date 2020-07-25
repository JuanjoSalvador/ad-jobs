from flask import abort, render_template, request
from . import admin_bp

@admin_bp.route('/login',methods=['GET', 'POST'])
def login():
    return render_template("login.jinja")

@admin_bp.route('/admin',methods=['GET'])
def admin():
    return render_template("admin.jinja", hide_footer = True)