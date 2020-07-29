from flask import render_template, request
from app.models import Offers
from app import db

from . import admin_bp

@admin_bp.route('/login',methods=['GET', 'POST'])
def login():
    return render_template("login.jinja")

@admin_bp.route('/admin',methods=['GET'])
def admin():
    offers = Offers.get_last_offers()
    return render_template("admin_dashboard.jinja", offers = offers)

@admin_bp.route('/admin/inbox', methods=['GET'], defaults={'page': 1})
@admin_bp.route("/admin/inbox/<page>", methods=['GET', 'POST'])
def inbox(page):
    offers = Offers.get_all()
    return render_template("admin_inbox.jinja", offers = offers)

@admin_bp.route("/admin/details/<id>", methods=['GET', 'POST'])
def details(id):
    offer = Offers.get_by_id(id)
    offer_id = id
    return render_template("admin_offer_detail.jinja", offer = offer, offer_id = offer_id)

@admin_bp.route("/admin/details/<id>/valid")
def validate_offer(id):
    offer = Offers.query.filter_by(id=id).first()
    offer.approbed = True
    db.session.commit()
    return ('', 200)
