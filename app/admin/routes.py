from flask import abort, render_template, request
from . import admin_bp

@admin_bp.route('/admin',methods=['GET', 'POST'])
def admin():
    return render_template("admin.jinja")