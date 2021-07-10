from app.utils import bad_request, response, not_found
from werkzeug.security import generate_password_hash
from app import db
from app.models import User as UserModel, Code

class User():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def register_user(data):
        try:
            email = data.get('email')
            password = data.get('password')
            first_name = data.get('first_name')
            last_name = data.get('last_name')

            if len(password) < 8 or email is None:
                return bad_request("Password must be at least 8 characters.")
            password = generate_password_hash(password, method='sha256')

            user = UserModel.query.filter_by(email=email).first()
            if not user:
                UserModel(email=email, 
                    password=password, 
                    first_name= first_name, 
                    last_name = last_name,
                )
                db.session.add(user)
                db.session.commit()
                return response()
            else:
                return bad_request("Email already exists.")
        except Exception as e:
            return bad_request(e)
    