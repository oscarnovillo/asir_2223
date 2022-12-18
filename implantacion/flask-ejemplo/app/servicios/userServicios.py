from app.data.modelo.user import User
from app.data.userDao import UserDao


class UserServicios:
    
    def __init__(self,db):
        self.db = UserDao(db.session)
        self.model = User
    
    def get_all(self):
        return self.db.get_all()
    