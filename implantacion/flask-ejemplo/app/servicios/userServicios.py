from app.data.modelo.user import User
from app.data.userDao import UserDao


class UserServicios:
    def __init__(self, db):
        self.userDao = UserDao(db.session)
        self.model = User

    def get_all(self):
        return self.userDao.get_all()

    def get_user_by_id(self, user_id: int):
        return self.userDao.get_user_by_id(user_id)

    def add_user(self, user: User):
        return self.userDao.add_user(user)
