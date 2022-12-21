from sqlalchemy.orm import Session

from app.data.modelo.user import User


class UserDao:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list:
        return self.session.query(User).all()

    def get_user_by_id(self, user_id : int)-> list:
        return self.session.query(User).get(user_id)

    def add_user(self, user: User):
        self.session.add(user)
        self.session.query()
        self.session.commit()
        return user
