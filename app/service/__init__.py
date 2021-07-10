from app.models import User as UserModel

def find_user_by_email(email):
    user = UserModel.query.filter_by(email=email).first()
    return user