from operator import itemgetter

from flask import Blueprint
from flask import request
from flask import make_response

from conduit.temp.tempdb import login_table
from conduit.temp.tempdb import user_table

bp = Blueprint("user", __name__)

login_data = login_table
user_data = user_table


@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        # will be hashed when actual password
        username, password = itemgetter("username", "password")(request.json)

        username_found = False
        password_found = False

        userid = None

        for login_user in login_table:
            if login_user["username"] == username:
                username_found = True
                if login_user["password"] == password:
                    password_found = True

                    userid = login_user["userid"]

        if username_found and password_found:
            print(userid)
            return make_response(({"userid": userid}, 200))
        elif not username_found:
            return make_response(({"error": "Username doesn't exist!"}, 500))
        elif not password_found:
            return make_response(({"error": "Password doesn't match!"}, 500))
    return ""
