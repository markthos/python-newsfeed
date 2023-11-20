from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        # Make sure email address contains @ character
        assert '@' in email
        return email

    @validates('password')
    def validate_password(self, key, password):
        # Make sure password is at least 5 characters long
        assert len(password) > 4
        # Hash the password with a unique salt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
