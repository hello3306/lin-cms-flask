"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint
from app.api.v1 import book, user


def create_v1():
    bp_v1 = Blueprint('v1', __name__)
    reds = [book, user]
    for red in reds:
        red.api.register(bp_v1)
    # book.book_api.register(bp_v1)
    # user.api.register(bp_v1)
    return bp_v1
