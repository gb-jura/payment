from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models.payment import Payment
from app import db

payment = Blueprint('payment', __name__)

@payment.route('/payments')
@login_required
def payments():
    payments = Payment.query.filter_by(user_id=current_user.id).all()
    return render_template('payments.html', payments=payments)
