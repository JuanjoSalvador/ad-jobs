from flask import render_template, request
from . import admin_bp

@admin_bp.route('/login',methods=['GET', 'POST'])
def login():
    return render_template("login.jinja")

@admin_bp.route('/admin',methods=['GET'])
def admin():
    return render_template("admin_dashboard.jinja", hide_footer = True)

@admin_bp.route('/admin/inbox', methods=['GET'], defaults={'page': 1})
@admin_bp.route("/admin/inbox/<int:page>", methods=['GET', 'POST'])
def inbox(page):
    return render_template("admin_inbox.jinja")

@admin_bp.route("/admin/details/<int:offer_id>", methods=['GET', 'POST'])
def details(offer_id):
    return render_template("admin_offer_detail.jinja")