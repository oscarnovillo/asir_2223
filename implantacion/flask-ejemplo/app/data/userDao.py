from sqlalchemy.orm import Session

from app.data.modelo.user import User


class UserDao:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list:
        return self.session.query(User).all()

    def get_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first

    def add_user(self, user: User):
        self.session.add(user)
        self.session.commit()
