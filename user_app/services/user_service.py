"""
This class has all the users operation and services
"""
import datetime
import traceback

from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker
from sql_app import crud
from sql_app.database import engine
from sql_app.models import User
from user_app.user_schema import UserInput, UserType
from user_app.services.auth_service import AuthService
from utility import response_obj


class UserService:

    def register_user(self, payload: UserInput):
        Session = sessionmaker(bind=engine)
        session = Session()
        email = payload.email
        user = session.query(User).filter(User.email == email).first()
        if user:
            raise Exception('User already exist')
        else:
            auth_service = AuthService()
            hashed_password = auth_service.encode_password(payload.password)
            last_login=datetime.datetime.now()
            db_user = User(email=email, password=hashed_password, last_login=last_login)
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            print(email)
            access_token = auth_service.encode_token(email)
            refresh_token = auth_service.encode_refresh_token(email)
            resp_data = {'accessToken': access_token, 'refreshToken': refresh_token,'email':email}
            print(resp_data)
            return UserType(email=email, accessToken=access_token,refreshToken=refresh_token,lastLogin=last_login)


    # def get_all_user(self):
    #     users = crud.get_users(self.__db, skip= 0, limit=100)
    #     return users

    # def retrieve_user(self):
    #     db_user = crud.get_user(self.__db, user_id=self.__user)
    #     if db_user is None:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return db_user
    #
    def signin_user(self, payload: UserInput):
        auth_service = AuthService()

        Session = sessionmaker(bind=engine)
        session = Session()
        email = payload.email

        try:
            user = session.query(User).filter(User.email == email).first()
            if user is None:
                raise Exception('user not found')
            if auth_service.verify_password(password=payload.password,encoded_password=user.password):
                last_login = datetime.datetime.now()
                user.last_login =last_login
                session.commit()
                access_token = auth_service.encode_token(payload.email)
                refresh_token = auth_service.encode_refresh_token(payload.email)
                print(access_token)
                return UserType(email=email, accessToken=access_token,refreshToken=refresh_token,lastLogin=datetime.datetime.now())
            else:
                raise Exception('wrong password')
        except Exception as e:
            traceback.print_exc()
            raise Exception(e.__str__())



