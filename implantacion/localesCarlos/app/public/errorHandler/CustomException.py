from typing import Optional, Text

from flask_api import status
from werkzeug.exceptions import HTTPException


class CustomException(HTTPException):
    code = status.HTTP_409_CONFLICT
    description = "mensaje"

    def __init__(self, description: Optional[Text] = ..., code: Optional[int] = ...) -> None:
        # Ellipsis es cuando no se envia el parametro
        if (code is not Ellipsis):
            self.code = code
        super().__init__(description)

    # def get_response(self):
