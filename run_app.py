from flask import request

from conduit.app import create_app

app = create_app()


@app.route("/")
def index():
    return "<h1>hi there! You are viewing an index of a server. go away fam</h1>"


@app.after_request
def after_request_func(response):
    if not request.path == "/":
        response.headers["Content-Type"] = "application/json"

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)