from flask import Blueprint, render_template

import utils
from services import user_service, access_service

blueprint = Blueprint('admin', __name__)

@blueprint.route('/dashboard', methods=['GET'])
def dashboard():
    users = user_service.get_registered_users()
    return render_template("dashboard.html",
                           users=users)

@blueprint.route('/user/<uuid>', methods=['GET'])
def details(uuid):
    user = user_service.get_user_by_uuid(uuid)
    access_dist = access_service.get_user_access_distribution(uuid)
    return render_template("access_history.html",
                           user=user,
                           access_dist=access_dist)