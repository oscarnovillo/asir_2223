from flask_restful.representations import json


def handle_custom_exception(e):
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "mensaje": e.description
    })
    response.content_type = "application/json"
    return response