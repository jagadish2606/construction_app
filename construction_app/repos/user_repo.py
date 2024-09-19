from construction_app.models.user import User

class UserRepository:

    def create_user(self, db, user):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
