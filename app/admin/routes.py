from flask import abort, render_template, request
from . import admin_bp

@admin_bp.route('/login',methods=['GET', 'POST'])
def login():
    return render_template("admin.jinja")