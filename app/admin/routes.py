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
    count = Offers.get_last_offers().count()
    total_offers = len(Offers.get_all())
    published = Offers.get_approbed().count()
    rejected = Offers.get_rejected().count()
    return render_template("admin_dashboard.jinja", 
            offers = offers, count = count, total_offers = total_offers,
            published = published, rejected = rejected
        )

@admin_bp.route('/admin/inbox', methods=['GET'], defaults={'page': 1})
#@admin_bp.route("/admin/inbox/<page>", methods=['GET', 'POST'])
def inbox(page):
    offers = Offers.get_not_reviewed()
    count = Offers.get_not_reviewed().count()
    return render_template("admin_inbox.jinja", offers = offers, count = count)

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

@admin_bp.route("/admin/details/<id>/invalid")
def reject_offer(id):
    offer = Offers.query.filter_by(id=id).first()
    offer.approbed = False
    db.session.commit()
    return ('', 200)

@admin_bp.route("/admin/details/<id>/remove")
def remove_offer(id):
    offer = Offers.query.filter_by(id=id).first()
    offer.approbed = None
    db.session.commit()
    return ('', 200)
    